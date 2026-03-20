# 📦 GitHub 上传文件包

这个目录包含了所有需要上传到 GitHub 的文件。

## 📋 文件清单

### ✅ 必须上传的文件

```
├── .github/
│   └── workflows/
│       └── twitter-bot.yml          ← GitHub Actions 配置文件
│
├── src/
│   ├── tools/
│   │   ├── __init__.py              ← Python 包初始化文件
│   │   ├── google_sheets_tool.py    ← Google Sheets 工具
│   │   └── twitter_tool.py          ← Twitter API 工具
│   │
│   └── utils/
│       ├── __init__.py              ← Python 包初始化文件
│       └── post_utils.py            ← 推文格式化工具
│
├── send_post.py                     ← 主程序文件
└── requirements.txt                 ← Python 依赖配置
```

### 📚 可选上传的文件（建议上传）

```
docs/
├── BEGINNER_TUTORIAL.md             ← 小白入门教程
├── CONFIGURATION_CHECKLIST.md       ← 配置检查清单
├── GITHUB_UPLOAD_GUIDE.md           ← 上传指南
├── GOOGLE_CREDENTIALS_GUIDE.md      ← Google 凭证获取指南
├── QUICK_START.md                   ← 快速开始指南
├── TEST_GUIDE.md                    ← 测试指南
└── TWITTER_API_KEYS_GUIDE.md        ← Twitter API 密钥指南
```

## 🚀 上传步骤

### 步骤 1：创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写信息：
   - Repository name: `twitter-bot`
   - Description: `Twitter auto-post bot`
   - 选择 **Private**（私有仓库）
   - **不要**勾选任何初始化选项
3. 点击 "Create repository"

### 步骤 2：上传文件

**方法一：网页上传（推荐新手）**

1. 在仓库页面，点击 "uploading an existing file"
2. 将本目录下的所有文件和文件夹拖拽到上传区域
3. 保持目录结构不变
4. 点击 "Commit changes"

**方法二：使用 Git 命令行**

```bash
# 初始化仓库
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: Twitter bot project"

# 关联远程仓库
git remote add origin https://github.com/你的用户名/twitter-bot.git

# 推送
git push -u origin main
```

### 步骤 3：配置 GitHub Secrets

上传完成后，需要配置 GitHub Secrets（详见下方说明）。

## ⚠️ 重要提醒

### ❌ 绝对不要上传到 GitHub 的文件

- Twitter API 密钥文件
- Google 凭证 JSON 文件
- `.env` 文件
- 任何包含密钥的文件

### ✅ 这些信息应该配置在 GitHub Secrets 中

你需要配置以下 Secrets：

1. `TWITTER_API_KEY` - Twitter API Key
2. `TWITTER_API_SECRET` - Twitter API Secret
3. `TWITTER_ACCESS_TOKEN` - Twitter Access Token
4. `TWITTER_ACCESS_TOKEN_SECRET` - Twitter Access Token Secret
5. `GOOGLE_SPREADSHEET_ID` - Google Sheet ID
6. `GOOGLE_CREDENTIALS_JSON` - Google 凭证 JSON 的完整内容

## 📖 详细教程

- **新手入门**：查看 `docs/BEGINNER_TUTORIAL.md`
- **配置检查清单**：查看 `docs/CONFIGURATION_CHECKLIST.md`
- **测试指南**：查看 `docs/TEST_GUIDE.md`

## 🎯 下一步

1. 上传所有文件到 GitHub
2. 配置 GitHub Secrets
3. 在 Google Sheet 中添加测试数据（发送状态设为"未发送"）
4. 手动触发 GitHub Actions 进行测试
5. 查看运行结果

祝你使用愉快！🚀
