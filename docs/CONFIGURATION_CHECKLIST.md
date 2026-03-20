# ✅ 配置检查清单

> 在开始之前，请按照此清单逐项检查，确保所有配置都正确。

## 📋 第一阶段：账号准备

### 1. Twitter 账号
- [ ] 我有 Twitter 账号
- [ ] 账号用户名：`@_____________`
- [ ] 账号可以正常登录和使用

### 2. Google 账号
- [ ] 我有 Google 账号
- [ ] 账号邮箱：`_____________`
- [ ] 可以访问 Google Drive 和 Google Sheets

### 3. GitHub 账号
- [ ] 我有 GitHub 账号
- [ ] 用户名：`_____________`
- [ ] 可以创建仓库

---

## 📋 第二阶段：Twitter API 配置

### 4. 开发者账号申请
- [ ] 已访问 https://developer.twitter.com
- [ ] 已登录 Twitter 账号
- [ ] 已提交开发者账号申请
- [ ] 申请已通过审核（邮箱收到确认）

### 5. 创建 Twitter 应用
- [ ] 已创建项目和应用
- [ ] 项目名称：`_____________`
- [ ] 应用名称：`_____________`

### 6. 获取 API 密钥 ⚠️ 重要
请复制并保存以下信息：

- [ ] **API Key**（Consumer Key）
  ```
  _______________________________
  ```

- [ ] **API Key Secret**（Consumer Secret）
  ```
  _______________________________
  ```

- [ ] **Access Token**
  ```
  _______________________________
  ```

- [ ] **Access Token Secret**
  ```
  _______________________________
  ```

### 7. 权限设置 ⚠️ 非常重要
- [ ] 已设置应用权限为"Read and Write"
- [ ] 已重新生成 Access Token（修改权限后必须重新生成）

---

## 📋 第三阶段：Google Cloud 配置

### 8. 创建 Google Cloud 项目
- [ ] 已访问 https://console.cloud.google.com
- [ ] 已创建新项目
- [ ] 项目名称：`_____________`
- [ ] 项目 ID：`_____________`

### 9. 启用 API
- [ ] 已启用 Google Sheets API
- [ ] 已启用 Google Drive API

### 10. 创建服务账号
- [ ] 已创建服务账号
- [ ] 服务账号名称：`_____________`
- [ ] 服务账号邮箱：`_____________@_____________.iam.gserviceaccount.com`

### 11. 创建服务账号密钥 ⚠️ 非常重要
- [ ] 已创建 JSON 密钥
- [ ] JSON 文件已下载到本地
- [ ] JSON 文件路径：`_____________`
- [ ] JSON 文件已妥善保存（不要丢失！）

### 12. 复制 JSON 内容 ⚠️ 关键步骤
请打开 JSON 文件，确认包含以下字段：

- [ ] `"type": "service_account"`
- [ ] `"project_id": "_____________"`
- [ ] `"private_key_id": "_____________"`
- [ ] `"private_key": "-----BEGIN PRIVATE KEY-----..."`
- [ ] `"client_email": "_____________@_____________.iam.gserviceaccount.com"`

**已复制完整 JSON 内容**：[ ]
（后面配置 GitHub Secrets 时需要粘贴整个 JSON 内容）

---

## 📋 第四阶段：Google Sheet 配置

### 13. 创建 Google Sheet
- [ ] 已创建新的 Google Sheet
- [ ] 表格名称：`_____________`

### 14. 设置列标题
第一行包含以下列（顺序和名称必须完全一致）：

- [ ] A列：`标题`
- [ ] B列：`DOI链接`
- [ ] C列：`TOC图片`
- [ ] D列：`发送状态`
- [ ] E列：`发送时间`
- [ ] F列：`推文ID`

### 15. 添加测试数据
第二行（测试文章）：

- [ ] 标题：`Deep Learning for Natural Language Processing`
- [ ] DOI链接：`https://doi.org/10.1234/test2024`
- [ ] TOC图片：（留空或填 `toc1.jpg`）
- [ ] 发送状态：`未发送`
- [ ] 发送时间：（留空）
- [ ] 推文ID：（留空）

### 16. 获取 Spreadsheet ID
从 Google Sheet URL 中提取 ID：

- [ ] URL：`https://docs.google.com/spreadsheets/d/_____________/edit`
- [ ] Spreadsheet ID：`_______________________________`

### 17. 分享给服务账号 ⚠️ 必须步骤
- [ ] 已点击 Google Sheet 的"共享"按钮
- [ ] 已添加服务账号邮箱（从 JSON 文件的 client_email 字段获取）
- [ ] 权限设置为"编辑者"
- [ ] 已点击"发送"

---

## 📋 第五阶段：GitHub 配置

### 18. 准备代码仓库
- [ ] 已创建 GitHub 仓库
- [ ] 仓库名称：`_____________`
- [ ] 仓库可见性：[ ] Public [ ] Private（建议 Private）
- [ ] 已上传所有代码文件

### 19. 检查文件结构
确保仓库包含以下文件：

- [ ] `.github/workflows/twitter-bot.yml`
- [ ] `send_post.py`
- [ ] `src/tools/google_sheets_tool.py`
- [ ] `src/tools/twitter_tool.py`
- [ ] `src/utils/post_utils.py`
- [ ] `requirements.txt`

### 20. 配置 GitHub Secrets ⚠️ 最重要步骤

进入仓库 Settings > Secrets and variables > Actions，添加以下 secrets：

#### Secret 1
- [ ] Name: `TWITTER_API_KEY`
- [ ] Value: `[粘贴你的 Twitter API Key]`
- [ ] 状态：已添加

#### Secret 2
- [ ] Name: `TWITTER_API_SECRET`
- [ ] Value: `[粘贴你的 Twitter API Secret]`
- [ ] 状态：已添加

#### Secret 3
- [ ] Name: `TWITTER_ACCESS_TOKEN`
- [ ] Value: `[粘贴你的 Access Token]`
- [ ] 状态：已添加

#### Secret 4
- [ ] Name: `TWITTER_ACCESS_TOKEN_SECRET`
- [ ] Value: `[粘贴你的 Access Token Secret]`
- [ ] 状态：已添加

#### Secret 5
- [ ] Name: `GOOGLE_SPREADSHEET_ID`
- [ ] Value: `[粘贴你的 Spreadsheet ID]`
- [ ] 状态：已添加

#### Secret 6 ⚠️ 最关键
- [ ] Name: `GOOGLE_CREDENTIALS_JSON`
- [ ] Value: `[粘贴完整的 JSON 文件内容，保持单行]`
- [ ] 状态：已添加

### 21. 验证 Secrets
- [ ] 已添加 6 个 Secrets
- [ ] 每个 Secret 的值都已确认正确
- [ ] 特别是 GOOGLE_CREDENTIALS_JSON 是完整的 JSON 内容

---

## 📋 第六阶段：测试运行

### 22. 手动触发
- [ ] 已进入仓库的 Actions 标签页
- [ ] 已选择"Twitter Bot" workflow
- [ ] 已点击"Run workflow"
- [ ] 已确认运行开始

### 23. 查看运行结果
- [ ] 运行状态：[ ] ✅ 成功 [ ] ❌ 失败
- [ ] 如失败，错误信息：`_____________`

### 24. 验证推文
- [ ] 已打开 Twitter 主页
- [ ] 看到新发布的推文
- [ ] 推文内容正确
- [ ] 图片显示正常（如果有图片）

### 25. 验证 Google Sheet 更新
- [ ] 已打开 Google Sheet
- [ ] 第二行状态已更新为"已发送"
- [ ] 发送时间已填写
- [ ] 推文 ID 已填写

---

## 🎯 检查结果

### 全部完成！

如果所有复选框都已勾选，恭喜你已经成功配置好系统！

### 遇到问题？

如果某些步骤失败，请：

1. **查看 Actions 日志**
   - 详细的错误信息是解决问题的关键
   - 复制错误信息，便于排查

2. **逐步排查**
   - 按照"配置检查清单"重新检查每一步
   - 特别关注标记⚠️的重要步骤

3. **常见错误**
   - Twitter API 认证失败：检查密钥和权限
   - Google Sheet 连接失败：检查分享权限
   - 找不到文件：检查文件结构和路径

---

## 📝 配置信息汇总

**Twitter 信息**
- 用户名：`_____________`
- API Key：`_____________`
- API Secret：`_____________`
- Access Token：`_____________`
- Access Token Secret：`_____________`

**Google Cloud 信息**
- 项目名称：`_____________`
- 服务账号邮箱：`_____________`
- JSON 文件路径：`_____________`

**Google Sheet 信息**
- 表格名称：`_____________`
- Spreadsheet ID：`_____________`

**GitHub 信息**
- 仓库地址：`_____________`
- 仓库名称：`_____________`

---

## 💾 备份建议

请将以上信息保存到安全的地方：
- [ ] 已保存到本地文档
- [ ] 已保存到密码管理器
- [ ] JSON 文件已备份

**⚠️ 安全提醒**
- 不要将敏感信息上传到 GitHub
- 不要在公开场合分享密钥
- 定期更新 API 密钥

---

最后更新时间：`_____________`
