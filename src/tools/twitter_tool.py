"""
Twitter API 封装工具
提供认证、图片上传、发布推文等功能
"""

import logging
from typing import Optional
import tweepy
from io import BytesIO
from PIL import Image

logger = logging.getLogger(__name__)


class TwitterClient:
    """Twitter客户端封装"""

    def __init__(self, api_key: str, api_secret: str, access_token: str, access_token_secret: str):
        """
        初始化Twitter客户端

        Args:
            api_key: Twitter API Key
            api_secret: Twitter API Secret
            access_token: Twitter Access Token
            access_token_secret: Twitter Access Token Secret
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.api = None
        self.client = None
        self._username = None

    def login(self) -> bool:
        """
        登录Twitter

        Returns:
            bool: 登录是否成功
        """
        try:
            # 认证
            auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
            auth.set_access_token(self.access_token, self.access_token_secret)

            # 创建 API 客户端 (v1.1)
            self.api = tweepy.API(auth)

            # 创建客户端 (v2)
            self.client = tweepy.Client(
                consumer_key=self.api_key,
                consumer_secret=self.api_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret
            )

            # 验证凭证
            user = self.client.get_me()
            if user and user.data:
                self._username = user.data.username
                logger.info(f"Twitter登录成功: @{self._username}")
                return True
            else:
                logger.error("无法获取用户信息")
                return False

        except Exception as e:
            logger.error(f"Twitter登录失败: {str(e)}")
            return False

    def _optimize_image(self, image_bytes: bytes, max_size_mb: int = 5) -> bytes:
        """
        优化图片，确保符合Twitter的限制

        Twitter图片限制：
        - 最大5MB (免费账号)
        - 最大15MB (认证账号)
        - 支持格式: JPG, PNG, GIF, WebP

        Args:
            image_bytes: 原始图片二进制数据
            max_size_mb: 最大文件大小（MB），默认5MB

        Returns:
            bytes: 优化后的图片二进制数据
        """
        # 检查文件大小
        file_size_mb = len(image_bytes) / (1024 * 1024)
        logger.info(f"原始图片大小: {file_size_mb:.2f}MB")

        # 如果已经符合大小限制，直接返回
        if file_size_mb <= max_size_mb:
            logger.info("图片大小符合要求，无需优化")
            return image_bytes

        try:
            # 打开图片
            img = Image.open(BytesIO(image_bytes))
            width, height = img.size
            logger.info(f"原始图片尺寸: {width}x{height}")

            # 转换为RGB模式（去除透明通道）
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[3])
                else:
                    background.paste(img)
                img = background
                logger.info("转换为RGB模式")

            # 逐步降低质量直到符合大小限制
            quality = 95
            while quality >= 70:
                output = BytesIO()
                img.save(output, format='JPEG', quality=quality, optimize=True)
                optimized_bytes = output.getvalue()

                if len(optimized_bytes) <= max_size_mb * 1024 * 1024:
                    logger.info(f"优化完成: 质量={quality}, 大小={len(optimized_bytes) / (1024 * 1024):.2f}MB")
                    return optimized_bytes

                quality -= 5

            # 如果还是太大，尝试缩小尺寸
            scale = 0.9
            while scale >= 0.3:
                new_width = int(width * scale)
                new_height = int(height * scale)
                resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                output = BytesIO()
                resized_img.save(output, format='JPEG', quality=85, optimize=True)
                optimized_bytes = output.getvalue()

                if len(optimized_bytes) <= max_size_mb * 1024 * 1024:
                    logger.info(f"优化完成: 尺寸={new_width}x{new_height}, 大小={len(optimized_bytes) / (1024 * 1024):.2f}MB")
                    return optimized_bytes

                scale -= 0.1

            logger.warning(f"无法优化到指定大小，返回原始图片")
            return image_bytes

        except Exception as e:
            logger.error(f"图片优化失败: {str(e)}")
            return image_bytes

    def send_tweet(self, text: str) -> Optional[str]:
        """
        发布纯文本推文

        Args:
            text: 推文文本（最多280字符）

        Returns:
            Optional[str]: 推文ID，失败返回None
        """
        try:
            # 检查字符数限制
            if len(text) > 280:
                logger.warning(f"推文超过280字符 ({len(text)}), 将被截断")
                text = text[:277] + "..."

            # 发布推文
            response = self.client.create_tweet(text=text)

            if response and response.data:
                tweet_id = response.data['id']
                logger.info(f"推文发布成功: {tweet_id}")
                return tweet_id
            else:
                logger.error("推文发布失败: 无响应数据")
                return None

        except Exception as e:
            logger.error(f"推文发布失败: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return None

    def send_tweet_with_image(self, text: str, image_bytes: bytes, image_alt: str = "TOC Image") -> Optional[str]:
        """
        发布带图片的推文

        Args:
            text: 推文文本（最多280字符）
            image_bytes: 图片二进制数据
            image_alt: 图片alt文本（可选）

        Returns:
            Optional[str]: 推文ID，失败返回None
        """
        try:
            # 优化图片
            optimized_image = self._optimize_image(image_bytes)

            # 上传图片到Twitter (使用v1.1 API)
            media = self.api.media_upload(filename='toc.jpg', file=BytesIO(optimized_image))

            # 添加图片alt文本
            if image_alt:
                self.api.create_media_metadata(media.media_id, image_alt)

            # 发布推文 (使用v2 API)
            response = self.client.create_tweet(text=text, media_ids=[media.media_id])

            if response and response.data:
                tweet_id = response.data['id']
                logger.info(f"推文发布成功: {tweet_id}")
                return tweet_id
            else:
                logger.error("推文发布失败: 无响应数据")
                return None

        except Exception as e:
            logger.error(f"推文发布失败: {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
            return None

    def delete_tweet(self, tweet_id: str) -> bool:
        """
        删除推文

        Args:
            tweet_id: 推文ID

        Returns:
            bool: 删除是否成功
        """
        try:
            self.client.delete_tweet(id=tweet_id)
            logger.info(f"推文删除成功: {tweet_id}")
            return True
        except Exception as e:
            logger.error(f"推文删除失败: {str(e)}")
            return False
