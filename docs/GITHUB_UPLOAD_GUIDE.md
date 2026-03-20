# 📦 GitHub 上传文件清单

## ⚠️ 重要提醒

**不要上传敏感信息到 GitHub！**

❌ **绝对不要上传的文件**：
- Twitter API 密钥文件
- Google 凭证 JSON 文件（`credentials.json` 等）
- `.env` 环境变量文件
- 任何包含密钥的文件

✅ **这些信息应该存储在 GitHub Secrets 中**

---

## 📁 必须上传的文件

### 1. GitHub Actions 配置文件

**文件路径**：`.github/workflows/twitter-bot.yml`

**作用**：定义 GitHub Actions 的定时任务和运行流程

**内容**：已经创建在项目中，直接上传即可

---

### 2. 主程序文件

**文件路径**：`send_post.py`

**作用**：主程序入口，GitHub Actions 会运行这个文件

**内容**：已经创建在项目中，直接上传即可

---

### 3. 源代码文件（src 目录）

#### 3.1 Google Sheets 工具
**文件路径**：`src/tools/google_sheets_tool.py`

**作用**：读取和更新 Google Sheet 数据

**内容**：已经创建在项目中

---

#### 3.2 Twitter 工具
**文件路径**：`src/tools/twitter_tool.py`

**作用**：发布推文到 Twitter

**内容**：已经创建在项目中

---

#### 3.3 推文格式化工具
**文件路径**：`src/utils/post_utils.py`

**作用**：格式化推文内容

**内容**：已经创建在项目中

---

#### 3.4 包初始化文件
**文件路径**：
- `src/tools/__init__.py`
- `src/utils/__init__.py`

**作用**：Python 包初始化文件

**内容**：已经创建在项目中

---

### 4. 依赖配置文件

**文件路径**：`requirements.txt`

**作用**：定义项目依赖的 Python 包

**内容**：已经创建在项目中

---

## 📁 可选上传的文件

### 1. README 文件

**文件路径**：`README.md`

**作用**：项目说明文档

**内容**：建议上传，方便以后查看

---

### 2. 使用文档

**文件路径**：`docs/` 目录下的所有文件

**包含文件**：
- `docs/BEGINNER_TUTORIAL.md`（小白入门教程）
- `docs/CONFIGURATION_CHECKLIST.md`（配置检查清单）
- `docs/QUICK_START.md`（快速开始指南）
- `docs/TWITTER_API_KEYS_GUIDE.md`（Twitter API 密钥指南）
- `docs/GOOGLE_CREDENTIALS_GUIDE.md`（Google 凭证指南）
- `docs/TEST_GUIDE.md`（测试指南）

**作用**：帮助理解和配置项目

**建议**：全部上传

---

### 3. assets 目录（如果有图片）

**文件路径**：`assets/`

**作用**：存放 TOC 图片文件

**内容**：
- 图片文件（`.jpg`, `.png` 等）
- 示例图片

**建议**：如果暂时没有图片，可以先不上传

---

## 📋 完整的文件结构

你的 GitHub 仓库应该包含以下文件：

```
你的仓库/
├── .github/
│   └── workflows/
│       └── twitter-bot.yml          ✅ 必须
│
├── src/
│   ├── tools/
│   │   ├── __init__.py              ✅ 必须
│   │   ├── google_sheets_tool.py    ✅ 必须
│   │   └── twitter_tool.py          ✅ 必须
│   │
│   └── utils/
│       ├── __init__.py              ✅ 必须
│       └── post_utils.py            ✅ 必须
│
├── docs/                             ⭕ 可选（建议上传）
│   ├── BEGINNER_TUTORIAL.md
│   ├── CONFIGURATION_CHECKLIST.md
│   ├── QUICK_START.md
│   ├── TWITTER_API_KEYS_GUIDE.md
│   ├── GOOGLE_CREDENTIALS_GUIDE.md
│   └── TEST_GUIDE.md
│
├── assets/                           ⭕ 可选（如有图片）
│   └── *.jpg, *.png
│
├── send_post.py                      ✅ 必须
├── requirements.txt                  ✅ 必须
└── README.md                         ⭕ 可选（建议上传）
```

---

## 🚀 上传步骤

### 方式一：使用 GitHub 网页上传（适合小白）

#### 步骤 1：创建仓库

1. 访问 https://github.com/new
2. 填写信息：
   - Repository name: `twitter-bot`
   - Description: `Twitter auto-post bot`
   - 选择 **Private**（私有仓库更安全）
   - **不要**勾选 "Add a README file"
   - **不要**勾选 "Add .gitignore"
   - **不要**选择 License
3. 点击 "Create repository"

---

#### 步骤 2：上传文件

**方法 A：逐个上传**

1. 在仓库页面，点击 "Add file" > "Upload files"

2. **创建目录结构**：
   - 在文件名输入框中输入路径，如 `.github/workflows/twitter-bot.yml`
   - GitHub 会自动创建目录

3. **上传文件**：
   - 拖拽文件到上传区域
   - 或者点击 "choose your files" 选择文件

4. **提交更改**：
   - 在底部输入提交信息：`Add project files`
   - 点击 "Commit changes"

5. **重复以上步骤**，上传所有文件

---

**方法 B：批量上传（推荐）**

1. 在本地创建一个文件夹，按照上述目录结构组织所有文件

2. 将所有文件一次性拖拽到 GitHub 上传页面

3. 提交

---

### 方式二：使用 Git 命令行（适合有经验者）

```bash
# 1. 克隆仓库
git clone https://github.com/你的用户名/twitter-bot.git
cd twitter-bot

# 2. 复制文件到目录
# 将所有文件复制到对应的目录

# 3. 添加文件
git add .

# 4. 提交
git commit -m "Add project files"

# 5. 推送
git push origin main
```

---

## ✅ 上传检查清单

### 必须文件（共 7 个）

- [ ] `.github/workflows/twitter-bot.yml`
- [ ] `send_post.py`
- [ ] `src/tools/__init__.py`
- [ ] `src/tools/google_sheets_tool.py`
- [ ] `src/tools/twitter_tool.py`
- [ ] `src/utils/__init__.py`
- [ ] `src/utils/post_utils.py`
- [ ] `requirements.txt`

### 可选文件

- [ ] `README.md`
- [ ] `docs/BEGINNER_TUTORIAL.md`
- [ ] `docs/CONFIGURATION_CHECKLIST.md`
- [ ] `docs/QUICK_START.md`
- [ ] `docs/TWITTER_API_KEYS_GUIDE.md`
- [ ] `docs/GOOGLE_CREDENTIALS_GUIDE.md`
- [ ] `docs/TEST_GUIDE.md`
- [ ] `assets/` 目录（如有图片）

---

## 🆘 常见问题

### Q1: 如何在 GitHub 上创建文件夹？

**方法**：
- 在上传文件时，文件名输入 `文件夹名/文件名`
- 例如：`src/tools/google_sheets_tool.py`
- GitHub 会自动创建 `src/tools/` 文件夹

### Q2: 文件上传后看不到？

**可能原因**：
- 文件夹层级不对
- 文件名错误

**解决方法**：
- 检查文件结构是否符合要求
- 查看仓库的文件列表

### Q3: 可以上传压缩包吗？

**回答**：不建议

- GitHub 无法直接运行压缩包中的代码
- 需要解压后逐个上传

### Q4: 忘记上传某个文件怎么办？

**解决方法**：
- 随时可以继续上传
- 进入对应的文件夹，点击 "Add file" > "Upload files"
- 上传缺失的文件

---

## 📞 需要帮助？

如果你在上传过程中遇到问题：

1. **告诉我具体问题**
   - 上传了哪些文件
   - 看到什么错误提示
   - 卡在哪一步

2. **截图**
   - 仓库文件列表截图
   - 错误提示截图

我会帮你解决！

---

## 🎯 上传完成后

上传完成后，继续以下步骤：

1. **配置 GitHub Secrets**（你已经完成了）
2. **手动触发 Actions 测试**
3. **查看运行结果**

祝你上传顺利！🚀
