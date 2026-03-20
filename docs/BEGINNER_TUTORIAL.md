# 🎓 小白入门教程：Twitter 自动发文系统

> 这是一个从零开始的完整教程，假设你完全没有相关经验。

## 📚 目录

1. [第一部分：基本概念](#第一部分基本概念)
2. [第二部分：准备工作](#第二部分准备工作)
3. [第三部分：配置 Twitter](#第三部分配置-twitter)
4. [第四部分：配置 Google Sheet](#第四部分配置-google-sheet)
5. [第五部分：配置 GitHub](#第五部分配置-github)
6. [第六部分：测试运行](#第六部分测试运行)
7. [第七部分：日常使用](#第七部分日常使用)

---

## 第一部分：基本概念

### 什么是自动发文？

想象你有一个机器人，每天定时帮你发推文。你只需要提前准备好要发的内容，机器人会自动帮你发布。这就是自动发文系统。

### 需要准备什么？

1. **Twitter 账号**：你的推特账号（要发推文的账号）
2. **Twitter API 密钥**：相当于给你的机器人一把钥匙，让它能操作你的推特
3. **Google 账号**：用来创建 Google Sheet 存储文章数据
4. **GitHub 账号**：用来运行自动化程序
5. **Google Cloud 账号**：用来给机器人访问 Google Sheet 的权限

### 整体流程是什么？

```
你在 Google Sheet 填写文章
        ↓
GitHub 定时检查 Google Sheet
        ↓
发现新文章，自动发推文
        ↓
更新 Google Sheet 状态为"已发送"
```

---

## 第二部分：准备工作

### 步骤 1：创建 Twitter 账号（如果还没有）

1. 访问 https://twitter.com
2. 点击"注册"
3. 填写手机号或邮箱
4. 设置用户名和密码
5. 完成验证

**重要**：记住你的用户名（如 @yourname）

### 步骤 2：创建 Google 账号（如果还没有）

1. 访问 https://accounts.google.com
2. 点击"创建账号"
3. 填写个人信息
4. 完成验证

### 步骤 3：创建 GitHub 账号（如果还没有）

1. 访问 https://github.com
2. 点击"Sign up"
3. 填写邮箱、密码、用户名
4. 完成验证

---

## 第三部分：配置 Twitter

### 步骤 4：申请 Twitter 开发者账号

**什么是开发者账号？**
- 普通账号：只能你自己发推文
- 开发者账号：可以让程序帮你发推文

**操作步骤：**

1. **访问开发者门户**
   - 打开浏览器，访问：https://developer.twitter.com
   - 点击右上角"Sign in"，用你的 Twitter 账号登录

2. **申请开发者账号**
   - 登录后，点击"Sign up"或"Apply"
   - 选择" hobbyist"（爱好者）或"Making a bot"（制作机器人）
   - 选择最合适的选项：
     - 如果是个人使用，选" Hobbyist"
     - 如果是为了学习，选"Student"
     - 如果是为了制作机器人，选"Making a bot"

3. **填写申请表格**
   - **问题1**：What's your primary reason for wanting to access Twitter's APIs?
     - 翻译：你想要访问 Twitter API 的主要原因是什么？
     - 回答示例：`I want to automatically post academic paper announcements to my Twitter account. The posts will include paper titles, DOI links, and TOC images.`
   
   - **问题2**：Please describe how you plan to use Twitter data / API.
     - 翻译：请描述你打算如何使用 Twitter 数据/API。
     - 回答示例：`I will use the API to post tweets automatically from a Google Sheets database. Each tweet will contain a research paper title, DOI link, and an optional image. The system will post 2 tweets per day at scheduled times.`
   
   - **问题3**：Will your product, service, or analysis make Twitter content available to government entities?
     - 翻译：你的产品、服务或分析会将 Twitter 内容提供给政府实体吗？
     - 回答：`No`

4. **同意条款**
   - 勾选"I agree"
   - 点击"Submit application"

5. **等待审核**
   - 通常几小时到几天不等
   - 你会收到邮件通知

**💡 小贴士**：
- 申请理由要真实、具体
- 如果被拒绝，可以重新申请，提供更详细的说明
- 免费账号足够个人使用

### 步骤 5：创建 Twitter 应用

**审核通过后：**

1. **进入开发者门户**
   - 访问 https://developer.twitter.com/en/portal/dashboard
   - 你应该能看到一个仪表板

2. **创建项目和应用**
   - 点击左侧菜单"Projects & Apps"
   - 点击"+ Create Project"
   - **项目名称**：输入一个名称，如"My Twitter Bot"
   - **用例**：选择"Making a bot"
   - **项目描述**：输入描述，如"Auto post academic papers"

3. **创建应用**
   - 项目创建后，会自动提示创建应用
   - **应用名称**：输入名称，如"paper-bot"
   - 点击"Complete"

4. **获取 API 密钥**
   - 创建成功后，会显示"Keys and Tokens"
   - **重要**：这是你唯一一次看到这些密钥的机会！
   - 复制并保存以下信息：
     - `API Key`（也叫 Consumer Key）
     - `API Key Secret`（也叫 Consumer Secret）
   
   **⚠️ 重要提示**：
   - 立即复制这些密钥到安全的地方
   - 关闭页面后无法再次查看
   - 如果忘记了，只能重新生成

5. **生成 Access Token**
   - 在应用页面，找到"Keys and Tokens"标签
   - 找到"Access Token and Secret"部分
   - 点击"Generate"
   - 复制并保存：
     - `Access Token`
     - `Access Token Secret`

### 步骤 6：设置应用权限

**非常重要！否则无法发推文：**

1. **进入应用设置**
   - 在应用页面，点击"Settings"标签

2. **修改权限**
   - 找到"User authentication settings"
   - 点击"Set up"
   - **权限类型**：选择"Read and Write"
   - 点击"Save"

3. **重新生成 Token**
   - ⚠️ 修改权限后，之前的 Access Token 会失效
   - 回到"Keys and Tokens"标签
   - 点击"Regenerate"重新生成 Access Token
   - 保存新的 Token

**📝 检查清单**：
- ✅ API Key
- ✅ API Key Secret
- ✅ Access Token（读写权限）
- ✅ Access Token Secret

---

## 第四部分：配置 Google Sheet

### 步骤 7：创建 Google Cloud 项目

**什么是 Google Cloud？**
- Google 提供的云服务平台
- 我们需要它来给机器人访问 Google Sheet 的权限

**操作步骤：**

1. **访问 Google Cloud Console**
   - 打开浏览器，访问：https://console.cloud.google.com
   - 用你的 Google 账号登录

2. **创建新项目**
   - 点击顶部导航栏的项目选择器
   - 点击"新建项目"
   - **项目名称**：输入"twitter-bot"
   - 点击"创建"
   - 等待项目创建完成（约 10 秒）

3. **选择项目**
   - 点击顶部的项目选择器
   - 选择刚创建的"twitter-bot"项目

### 步骤 8：启用 Google Sheets API

1. **打开 API 库**
   - 在左侧菜单，点击"API 和服务" > "库"
   - 或直接访问：https://console.cloud.google.com/apis/library

2. **搜索并启用 API**
   - 在搜索框输入："Google Sheets API"
   - 点击搜索结果中的"Google Sheets API"
   - 点击"启用"
   
3. **启用 Google Drive API**
   - 再次搜索："Google Drive API"
   - 点击搜索结果
   - 点击"启用"

### 步骤 9：创建服务账号

**什么是服务账号？**
- 一个特殊的 Google 账号，给机器人用的
- 不是你自己的 Google 账号

**操作步骤：**

1. **打开服务账号页面**
   - 左侧菜单："IAM 和管理" > "服务账号"
   - 或直接访问：https://console.cloud.google.com/iam-admin/serviceaccounts

2. **创建服务账号**
   - 点击"创建服务账号"
   - **服务账号名称**：输入"twitter-bot-service"
   - 点击"创建并继续"

3. **设置权限**
   - 角色：选择"基本" > "Editor"
   - 点击"继续"
   - 点击"完成"

### 步骤 10：创建服务账号密钥

**这是最关键的一步！**

1. **打开服务账号详情**
   - 点击刚创建的服务账号邮箱
   - 进入"密钥"标签

2. **创建密钥**
   - 点击"添加密钥" > "创建新密钥"
   - 选择"JSON"
   - 点击"创建"
   
3. **保存密钥文件**
   - 浏览器会自动下载一个 JSON 文件
   - 文件名类似：`twitter-bot-xxxxx.json`
   - **⚠️ 非常重要**：
     - 这个文件包含敏感信息，千万不要泄露
     - 不要上传到 GitHub
     - 不要发给任何人
     - 妥善保存，后面会用到

### 步骤 11：创建 Google Sheet

1. **创建新表格**
   - 访问 https://sheets.google.com
   - 点击"空白"创建新表格

2. **设置列标题**（第一行）
   - 在 A1 单元格输入：`标题`
   - 在 B1 单元格输入：`DOI链接`
   - 在 C1 单元格输入：`TOC图片`
   - 在 D1 单元格输入：`发送状态`
   - 在 E1 单元格输入：`发送时间`
   - 在 F1 单元格输入：`推文ID`

3. **添加测试数据**（第二行）
   - A2: `Deep Learning for Natural Language Processing`
   - B2: `https://doi.org/10.1234/test2024`
   - C2: （留空，或填图片文件名如 `toc1.jpg`）
   - D2: `未发送`
   - E2: （留空）
   - F2: （留空）

4. **保存表格**
   - 按 `Ctrl + S`（Mac: `Cmd + S`）
   - 给表格命名，如"My Papers"

5. **获取 Spreadsheet ID**
   - 查看浏览器地址栏，URL 格式如下：
     ```
     https://docs.google.com/spreadsheets/d/这里是ID/edit
     ```
   - 复制 `d/` 和 `/edit` 之间的那段字符
   - 例如：`1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms`
   - 这就是你的 Spreadsheet ID，保存好

### 步骤 12：分享 Google Sheet 给服务账号

**这一步很重要，否则机器人无法访问表格！**

1. **打开 Google Sheet**
   - 打开你刚创建的表格

2. **点击分享**
   - 点击右上角的"共享"按钮

3. **添加服务账号**
   - 在"添加人员或群组"框中，粘贴服务账号邮箱
   - 服务账号邮箱在哪里？
     - 打开之前下载的 JSON 文件
     - 找到 `"client_email"` 这一行
     - 类似：`"client_email": "twitter-bot-service@twitter-bot.iam.gserviceaccount.com"`
     - 复制这个邮箱地址

4. **设置权限**
   - 权限选择："编辑者"
   - 取消勾选"通知对象"
   - 点击"发送"

**📝 检查清单**：
- ✅ Google Cloud 项目已创建
- ✅ Google Sheets API 已启用
- ✅ 服务账号已创建
- ✅ JSON 密钥文件已下载
- ✅ Google Sheet 已创建并添加数据
- ✅ Spreadsheet ID 已复制
- ✅ Google Sheet 已分享给服务账号

---

## 第五部分：配置 GitHub

### 步骤 13：Fork 或上传代码

**方式一：Fork 项目（推荐）**

1. 如果这个代码在你的 GitHub 仓库，直接使用
2. 如果在别人的仓库，点击右上角"Fork"

**方式二：创建新仓库**

1. **创建仓库**
   - 访问 https://github.com/new
   - 仓库名称：`twitter-bot`
   - 选择"Private"（私有仓库更安全）
   - 点击"Create repository"

2. **上传文件**
   - 点击"uploading an existing file"
   - 将所有文件拖拽上传
   - 点击"Commit changes"

### 步骤 14：配置 GitHub Secrets

**什么是 Secrets？**
- 加密存储敏感信息的地方
- 安全地存储你的密钥

**操作步骤：**

1. **打开仓库设置**
   - 进入你的 GitHub 仓库
   - 点击"Settings"（设置）标签

2. **找到 Secrets 设置**
   - 左侧菜单："Secrets and variables" > "Actions"

3. **添加以下 Secrets**（点击"New repository secret"）

   **Secret 1: TWITTER_API_KEY**
   - Name: `TWITTER_API_KEY`
   - Value: 粘贴你的 Twitter API Key
   - 点击"Add secret"

   **Secret 2: TWITTER_API_SECRET**
   - Name: `TWITTER_API_SECRET`
   - Value: 粘贴你的 Twitter API Secret
   - 点击"Add secret"

   **Secret 3: TWITTER_ACCESS_TOKEN**
   - Name: `TWITTER_ACCESS_TOKEN`
   - Value: 粘贴你的 Access Token
   - 点击"Add secret"

   **Secret 4: TWITTER_ACCESS_TOKEN_SECRET**
   - Name: `TWITTER_ACCESS_TOKEN_SECRET`
   - Value: 粘贴你的 Access Token Secret
   - 点击"Add secret"

   **Secret 5: GOOGLE_SPREADSHEET_ID**
   - Name: `GOOGLE_SPREADSHEET_ID`
   - Value: 粘贴你的 Google Spreadsheet ID
   - 点击"Add secret"

   **Secret 6: GOOGLE_CREDENTIALS_JSON**（最重要的一步！）
   - Name: `GOOGLE_CREDENTIALS_JSON`
   - Value: 
     1. 打开之前下载的 JSON 密钥文件
     2. 用文本编辑器打开（记事本即可）
     3. 全选并复制所有内容（Ctrl+A, Ctrl+C）
     4. 粘贴到 Value 框中
   - ⚠️ 注意：整个内容作为一行粘贴，不要格式化
   - 点击"Add secret"

**📝 检查清单**：
- ✅ TWITTER_API_KEY
- ✅ TWITTER_API_SECRET
- ✅ TWITTER_ACCESS_TOKEN
- ✅ TWITTER_ACCESS_TOKEN_SECRET
- ✅ GOOGLE_SPREADSHEET_ID
- ✅ GOOGLE_CREDENTIALS_JSON

---

## 第六部分：测试运行

### 步骤 15：手动触发测试

1. **打开 Actions 页面**
   - 进入你的 GitHub 仓库
   - 点击"Actions"标签

2. **选择 Workflow**
   - 左侧选择"Twitter Bot"
   - 点击右侧"Run workflow"
   - 确认分支是"main"或"master"
   - 点击绿色的"Run workflow"按钮

3. **查看运行日志**
   - 等待几秒，会出现一个新的运行记录
   - 点击这个运行记录
   - 查看"send-tweet"任务的日志
   - 点击任务名称查看详细日志

4. **检查结果**
   - 如果看到绿色的 ✅，说明成功
   - 如果看到红色的 ❌，说明有错误

### 步骤 16：检查推文

1. **打开 Twitter**
   - 访问你的 Twitter 主页
   - 刷新页面
   - 应该能看到新发布的推文

2. **检查 Google Sheet**
   - 打开你的 Google Sheet
   - 第二行的状态应该变为"已发送"
   - 发送时间应该被填写
   - 推文 ID 应该被填写

### 步骤 17：查看错误日志（如果失败）

**常见错误和解决方法：**

**错误 1：Twitter API 认证失败**
```
❌ Twitter登录失败: 401 Unauthorized
```
**解决方法**：
- 检查 TWITTER_API_KEY 和 TWITTER_API_SECRET 是否正确
- 检查 TWITTER_ACCESS_TOKEN 和 TWITTER_ACCESS_TOKEN_SECRET 是否正确
- 确认 Twitter 应用的权限是"Read and Write"
- 重新生成 Access Token

**错误 2：Google Sheet 连接失败**
```
❌ 连接Google Sheets失败
```
**解决方法**：
- 检查 GOOGLE_SPREADSHEET_ID 是否正确
- 检查 GOOGLE_CREDENTIALS_JSON 是否完整
- 确认服务账号邮箱已添加到 Google Sheet 的共享列表

**错误 3：没有找到未发送文章**
```
❌ 没有找到未发送的文章
```
**解决方法**：
- 这是正常的！说明所有文章都已发送
- 在 Google Sheet 中添加新文章，状态设为"未发送"

---

## 第七部分：日常使用

### 步骤 18：添加新文章

1. **打开 Google Sheet**

2. **添加新行**
   - 在下一行输入文章信息
   - 标题、DOI链接、TOC图片（可选）
   - 发送状态填"未发送"
   - 其他列留空

3. **等待自动发送**
   - GitHub Actions 会在设定时间自动发送
   - 或者你可以手动触发立即发送

### 步骤 19：修改发送时间

1. **打开 GitHub 仓库**

2. **编辑 Workflow 文件**
   - 点击 `.github/workflows/twitter-bot.yml`
   - 点击编辑按钮（铅笔图标）

3. **修改 cron 表达式**
   ```yaml
   on:
     schedule:
       # UTC时间 10:00（北京时间 18:00）
       - cron: '0 10 * * *'
       # UTC时间 16:00（北京时间 00:00）
       - cron: '0 16 * * *'
   ```

4. **时区转换**
   - 北京时间 = UTC 时间 + 8 小时
   - 例如：北京时间 20:00 = UTC 时间 12:00
   - cron 格式：`分钟 小时 * * *`

5. **保存修改**
   - 点击"Commit changes"

### 步骤 20：准备 TOC 图片（可选）

**方式一：上传到 GitHub**
1. 在仓库中创建 `assets` 文件夹
2. 上传图片文件（如 `toc1.jpg`）
3. 在 Google Sheet 的 TOC 图片列填写文件名：`toc1.jpg`

**方式二：使用图片 URL**
1. 将图片上传到图床（如 imgur.com）
2. 获取图片 URL
3. 在 Google Sheet 的 TOC 图片列填写完整 URL

---

## 🆘 常见问题

### Q1: 推文没有自动发送？

**检查以下几点：**
1. GitHub Actions 是否启用？
   - 进入仓库 Settings > Actions > General
   - 确保"Allow all actions"被选中

2. Workflow 文件是否正确？
   - 确认 `.github/workflows/twitter-bot.yml` 文件存在

3. 定时时间是否正确？
   - 检查 cron 表达式是否正确
   - 记住 GitHub 用的是 UTC 时间

### Q2: 推文内容乱码？

- 确保所有文件使用 UTF-8 编码
- 检查 Google Sheet 中的文字是否正确

### Q3: 图片没有显示？

**可能原因：**
1. 图片文件不存在
   - 检查 assets 目录下是否有该图片
   - 检查文件名是否匹配（区分大小写）

2. 图片 URL 无法访问
   - 确认 URL 可以正常访问
   - 某些网站有防盗链，建议上传到 GitHub

3. 图片太大
   - Twitter 限制图片最大 5MB
   - 程序会自动优化，但太大的图片可能失败

### Q4: 推文超过 280 字符？

- 程序会自动截断标题
- 建议标题控制在 150 字符以内
- 如果还超限，会自动去掉话题标签

### Q5: 忘记了某个密钥怎么办？

**Twitter 密钥：**
- 访问 https://developer.twitter.com/en/portal/dashboard
- 进入你的应用
- 在 Keys and Tokens 标签页可以重新生成

**Google 凭证：**
- 访问 Google Cloud Console
- 进入服务账号页面
- 创建新的 JSON 密钥

---

## 📞 需要帮助？

如果遇到问题：

1. **查看 Actions 日志**
   - 详细的错误信息会显示在日志中
   - 这是定位问题的最重要线索

2. **检查配置**
   - 再次检查所有 Secrets 是否正确
   - 确认 Google Sheet 已分享给服务账号

3. **手动测试**
   - 使用手动触发功能测试
   - 不要等待定时触发

---

## 🎉 恭喜！

如果你看到了推文成功发布，恭喜你已经成功搭建了自动发文系统！

**接下来你可以：**
- 在 Google Sheet 中批量添加文章
- 调整发送时间到最适合的时间
- 添加话题标签增加曝光
- 准备精美的 TOC 图片

**进阶功能：**
- 修改推文格式
- 添加多个话题标签
- 支持多个 Twitter 账号
- 添加更多自定义字段

祝你使用愉快！🚀
