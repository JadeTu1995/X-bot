"""
推文生成工具
"""


def format_tweet(title: str, doi_link: str, hashtags: str = None) -> str:
    """
    格式化推文内容

    Args:
        title: 文章标题
        doi_link: DOI链接
        hashtags: 话题标签（可选）

    Returns:
        str: 格式化后的推文内容
    """
    parts = [
        "📄 新文章发布",
        "",
        f"标题: {title}",
        f"DOI: {doi_link}"
    ]

    if hashtags:
        parts.append("")
        parts.append(hashtags)

    tweet = "\n".join(parts)

    # 检查字符数限制
    if len(tweet) > 280:
        # 截断标题
        base_length = len(tweet) - len(title)
        max_title_length = 280 - base_length - 3  # 预留3个字符给 "..."

        if max_title_length > 50:
            truncated_title = title[:max_title_length] + "..."
            parts[2] = f"标题: {truncated_title}"
            tweet = "\n".join(parts)
        else:
            # 如果连最短标题都不行，去掉标签
            if hashtags:
                parts = parts[:-2]  # 去掉标签部分
                tweet = "\n".join(parts)

                # 再次检查
                if len(tweet) > 280:
                    base_length = len(tweet) - len(title)
                    max_title_length = 280 - base_length - 3
                    truncated_title = title[:max_title_length] + "..."
                    parts[2] = f"标题: {truncated_title}"
                    tweet = "\n".join(parts)

    return tweet


def create_tweet_from_article(article: dict) -> str:
    """
    从文章字典创建推文内容

    Args:
        article: 文章字典，包含 '标题', 'DOI链接' 等字段

    Returns:
        str: 推文内容
    """
    title = article.get('标题', '')
    doi_link = article.get('DOI链接', '')
    hashtags = article.get('话题标签', '')

    return format_tweet(title, doi_link, hashtags)
