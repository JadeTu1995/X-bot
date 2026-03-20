"""
Twitter自动推文机器人 - 支持GitHub Actions自动运行
功能：从Google Sheets读取未发送文章，并发送到Twitter
"""
import sys
import os

# 设置工作目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.getcwd(), 'src'))

from dotenv import load_dotenv
load_dotenv()

print("=" * 70)
print("📋 步骤1：读取未发送文章")
print("=" * 70)
print()

from tools.google_sheets_tool import GoogleSheetsClient

client = GoogleSheetsClient(
    os.getenv("GOOGLE_CREDENTIALS_FILE", "credentials.json"),
    os.getenv("GOOGLE_SPREADSHEET_ID")
)

client.connect()
all_records = client.get_all_records()

# 找到第一条未发送的文章
article = None
for record in all_records:
    status = record.get('发送状态', '').strip()
    if status == '未发送':
        article = record
        break

if not article:
    print("❌ 没有找到未发送的文章")
    sys.exit(0)  # 没有文章不算错误

print(f"✅ 找到未发送文章")
print(f"   标题: '{article.get('标题', '')}'")
print(f"   DOI: '{article.get('DOI链接', '')}'")
print(f"   TOC图片: '{article.get('TOC图片', '')}'")
print()

row_number = client.get_row_number_by_index(all_records.index(article))
print(f"   行号: {row_number}")
print()

print("=" * 70)
print("📝 步骤2：生成推文内容")
print("=" * 70)
print()

title = article.get('标题', '')
doi_link = article.get('DOI链接', '')

if not title:
    print("❌ 标题为空")
    sys.exit(1)

from utils.post_utils import format_tweet
tweet_text = format_tweet(title, doi_link)

print(f"✅ 推文内容:")
print(f"   {tweet_text}")
print(f"   长度: {len(tweet_text)} 字符")
print()

# 检查字符数限制
if len(tweet_text) > 280:
    print("⚠️  推文超过280字符，将自动截断")
    # 截断标题
    max_title_length = 280 - len(tweet_text) + len(title) - 20
    if max_title_length > 50:
        truncated_title = title[:max_title_length] + "..."
        tweet_text = format_tweet(truncated_title, doi_link)
        print(f"   截断后推文: {tweet_text}")
    else:
        print("❌ 无法截断到合适长度")
        sys.exit(1)

print("=" * 70)
print("🖼️  步骤3：准备TOC图片")
print("=" * 70)
print()

toc_image_url = article.get('TOC图片', '').strip()
image_bytes = None

# 优先从assets目录读取
if toc_image_url:
    # 检查是否是文件名（不是URL）
    if not toc_image_url.startswith('http'):
        # 从assets目录读取（GitHub Actions兼容）
        image_path = os.path.join(os.getcwd(), 'assets', toc_image_url)
        print(f"从assets目录读取图片: {image_path}")

        if os.path.exists(image_path):
            try:
                with open(image_path, 'rb') as f:
                    image_bytes = f.read()
                print(f"✅ 图片加载成功")
                print(f"   大小: {len(image_bytes)} bytes")
            except Exception as e:
                print(f"❌ 图片加载失败: {str(e)}")
        else:
            print(f"❌ 文件不存在: {image_path}")
    else:
        # 从URL下载
        print(f"从URL下载图片: {toc_image_url}")
        print("正在下载图片...")

        try:
            import requests

            # 添加浏览器请求头，绕过防盗链
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

            response = requests.get(toc_image_url, headers=headers, timeout=30)
            response.raise_for_status()

            image_bytes = response.content
            print(f"✅ 图片下载成功")
            print(f"   大小: {len(image_bytes)} bytes")
        except Exception as e:
            print(f"❌ 图片下载失败: {str(e)}")

# 如果没有图片，直接发送不带图片的推文
if not image_bytes:
    print()
    print("⚠️  未找到TOC图片，将发送不带图片的推文")
    print()

print("=" * 70)
print("📱 步骤4：登录Twitter")
print("=" * 70)
print()

twitter_api_key = os.getenv("TWITTER_API_KEY")
twitter_api_secret = os.getenv("TWITTER_API_SECRET")
twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
twitter_access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

print(f"   API Key: {twitter_api_key[:10]}...")
print(f"   Access Token: {twitter_access_token[:10]}...")
print()

from tools.twitter_tool import TwitterClient

twitter_client = TwitterClient(
    api_key=twitter_api_key,
    api_secret=twitter_api_secret,
    access_token=twitter_access_token,
    access_token_secret=twitter_access_token_secret
)

if not twitter_client.login():
    print("❌ Twitter登录失败")
    print()
    print("可能的原因:")
    print("1. API密钥错误")
    print("2. Access Token过期")
    print("3. 网络连接问题")
    print("4. Twitter服务暂时不可用")
    sys.exit(1)

print(f"✅ Twitter登录成功")
print()

print("=" * 70)
print("🚀 步骤5：发送推文")
print("=" * 70)
print()

tweet_id = None
try:
    if image_bytes:
        print("正在发送推文（带TOC图片）...")
        tweet_id = twitter_client.send_tweet_with_image(
            text=tweet_text,
            image_bytes=image_bytes
        )
    else:
        print("正在发送推文（纯文本）...")
        tweet_id = twitter_client.send_tweet(text=tweet_text)

    if tweet_id:
        print(f"✅ 推文发送成功")
        print(f"   推文ID: {tweet_id}")
        print(f"   推文链接: https://twitter.com/user/status/{tweet_id}")
    else:
        print(f"❌ 推文发送失败")
        sys.exit(1)
except Exception as e:
    print(f"❌ 发送失败: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print()

print("=" * 70)
print("💾 步骤6：更新Google Sheets状态")
print("=" * 70)
print()

from datetime import datetime
send_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    success = client.update_article_status(
        row_number=row_number,
        status="已发送",
        send_time=send_time,
        tweet_id=tweet_id
    )

    if success:
        print(f"✅ 状态更新成功")
        print(f"   行号: {row_number}")
        print(f"   发送状态: 已发送")
        print(f"   发送时间: {send_time}")
        print(f"   推文ID: {tweet_id}")
    else:
        print(f"❌ 状态更新失败")
        sys.exit(1)
except Exception as e:
    print(f"❌ 状态更新错误: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print()
print("=" * 70)
print("✅ 全部完成！")
print("=" * 70)
print()
print("💡 推文效果:")
if image_bytes:
    print("   1. 文章标题")
    print("   2. DOI链接")
    print("   3. TOC图片")
else:
    print("   1. 文章标题")
    print("   2. DOI链接")

print()
print("🎉 推文发送成功！")
