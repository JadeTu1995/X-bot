# 🔑 Google Cloud 凭证获取指南

## 📍 你的 Spreadsheet ID

从你提供的网址：
```
https://docs.google.com/spreadsheets/d/1ncXdPO6ZNopnMxR_jB0s7fgOZTKxrSzE20OwQhFQ0To/edit
```

**Spreadsheet ID**：
```
1ncXdPO6ZNopnMxR_jB0s7fgOZTKxrSzE20OwQhFQ0To
```

---

## 🎯 目标：获取 GOOGLE_CREDENTIALS_JSON

这是从 Google Cloud Console 下载的 JSON 密钥文件。

---

## 📋 步骤 1：访问 Google Cloud Console

1. 打开浏览器
2. 访问：https://console.cloud.google.com
3. 用你的 Google 账号登录

---

## 📋 步骤 2：选择项目

1. 点击顶部导航栏的项目选择器（项目名称旁边）
2. 在弹出窗口中选择你之前创建的项目
   - 项目名称通常类似：`twitter-bot` 或其他你自定义的名称

**⚠️ 如果看不到任何项目**：

说明还没有创建项目，请先创建：

1. 点击项目选择器
2. 点击 "新建项目"
3. 项目名称：输入 `twitter-bot`
4. 点击 "创建"
5. 等待约 10 秒，项目创建完成
6. 选择这个新项目

---

## 📋 步骤 3：启用必要的 API

在创建服务账号之前，需要先启用 API。

### 3.1 打开 API 库

1. 点击左侧菜单 ☰
2. 选择 "API 和服务" > "库"
3. 或直接访问：https://console.cloud.google.com/apis/library

### 3.2 启用 Google Sheets API

1. 在搜索框输入：`Google Sheets API`
2. 点击搜索结果
3. 点击 "启用" 按钮

### 3.3 启用 Google Drive API

1. 再次搜索：`Google Drive API`
2. 点击搜索结果
3. 点击 "启用" 按钮

---

## 📋 步骤 4：创建服务账号

### 4.1 打开服务账号页面

**方式一**：通过菜单
1. 左侧菜单："IAM 和管理" > "服务账号"
2. 或直接访问：https://console.cloud.google.com/iam-admin/serviceaccounts

**方式二**：直接点击链接
- https://console.cloud.google.com/iam-admin/serviceaccounts

### 4.2 创建服务账号

1. 点击页面顶部的 "创建服务账号" 按钮

2. **第一步：服务账号详情**
   - 服务账号名称：`twitter-bot-service`
   - 服务账号 ID：会自动生成
   - 服务账号描述：（可选）`Twitter bot service account`
   - 点击 "创建并继续"

3. **第二步：授予访问权限**
   - 选择角色：点击 "选择角色"
   - 在搜索框输入：`Editor`
   - 选择："基本" > "Editor"（编辑者）
   - 点击 "继续"

4. **第三步：授予用户访问权限**
   - 这一步可以跳过
   - 直接点击 "完成"

---

## 📋 步骤 5：创建 JSON 密钥

### 5.1 打开服务账号详情

1. 在服务账号列表中，点击刚创建的服务账号邮箱
   - 邮箱类似：`twitter-bot-service@xxx.iam.gserviceaccount.com`

### 5.2 创建密钥

1. 点击 "密钥" 标签页
2. 点击 "添加密钥" > "创建新密钥"
3. 选择 "JSON"
4. 点击 "创建"

### 5.3 保存密钥文件

1. 浏览器会自动下载一个 JSON 文件
2. 文件名类似：`twitter-bot-123456-abc123.json`
3. **⚠️ 非常重要**：
   - 这个文件包含敏感信息，不要泄露
   - 不要上传到 GitHub
   - 不要发给任何人
   - 妥善保存，后面会用到

---

## 📋 步骤 6：查看 JSON 文件内容

### 方式一：用记事本打开

1. 找到下载的 JSON 文件
2. 右键点击 > "打开方式" > "记事本"
3. 你会看到类似这样的内容：

```json
{
  "type": "service_account",
  "project_id": "twitter-bot-123456",
  "private_key_id": "abc123def456...",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASC...\n-----END PRIVATE KEY-----\n",
  "client_email": "twitter-bot-service@twitter-bot-123456.iam.gserviceaccount.com",
  "client_id": "123456789012345678901",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/twitter-bot-service%40twitter-bot-123456.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

### 方式二：复制完整内容

1. 打开 JSON 文件
2. 按 `Ctrl + A`（全选）
3. 按 `Ctrl + C`（复制）

**这就是你要填入 GitHub Secrets 的 `GOOGLE_CREDENTIALS_JSON` 的值**

---

## 📋 步骤 7：分享 Google Sheet 给服务账号

**这一步最重要！** 不然机器人无法访问你的表格。

### 7.1 获取服务账号邮箱

从 JSON 文件中找到 `"client_email"` 字段：
```
"client_email": "twitter-bot-service@twitter-bot-123456.iam.gserviceaccount.com"
```

复制这个邮箱地址。

### 7.2 分享 Google Sheet

1. 打开你的 Google Sheet：
   https://docs.google.com/spreadsheets/d/1ncXdPO6ZNopnMxR_jB0s7fgOZTKxrSzE20OwQhFQ0To/edit

2. 点击右上角的 "共享" 按钮

3. 在 "添加人员或群组" 输入框中：
   - 粘贴服务账号邮箱：`twitter-bot-service@twitter-bot-123456.iam.gserviceaccount.com`

4. 设置权限：
   - 选择 "编辑者" 或 "Editor"
   - 取消勾选 "通知对象"

5. 点击 "发送"

---

## ✅ 检查清单

请逐项确认：

- [ ] 已访问 Google Cloud Console
- [ ] 已选择或创建项目
- [ ] 已启用 Google Sheets API
- [ ] 已启用 Google Drive API
- [ ] 已创建服务账号
- [ ] 已创建 JSON 密钥
- [ ] 已下载并保存 JSON 文件
- [ ] 已查看 JSON 文件内容
- [ ] 已复制服务账号邮箱
- [ ] 已将服务账号添加到 Google Sheet 共享列表

---

## 📝 配置信息汇总

### Spreadsheet ID
```
1ncXdPO6ZNopnMxR_jB0s7fgOZTKxrSzE20OwQhFQ0To
```

### 服务账号邮箱
```
[从 JSON 文件的 client_email 字段获取]
```

### JSON 密钥文件
```
文件位置：[你保存的路径]
文件内容：[整个 JSON 内容]
```

---

## 🎯 下一步：配置 GitHub Secrets

完成以上步骤后，你就有两个重要信息：

1. **GOOGLE_SPREADSHEET_ID**：
   ```
   1ncXdPO6ZNopnMxR_jB0s7fgOZTKxrSzE20OwQhFQ0To
   ```

2. **GOOGLE_CREDENTIALS_JSON**：
   - 整个 JSON 文件的内容（复制粘贴所有内容）

---

## 🆘 常见问题

### Q1: 我看不到 "服务账号" 菜单？

**原因**：可能是菜单折叠了

**解决**：
1. 点击左上角的 ☰ 图标
2. 展开菜单
3. 找到 "IAM 和管理" > "服务账号"

### Q2: 创建密钥时提示错误？

**可能原因**：
- 还没有启用必要的 API

**解决**：
1. 先去启用 Google Sheets API 和 Google Drive API
2. 然后再创建密钥

### Q3: JSON 文件内容很长，是不是正常的？

**回答**：是的，正常

- JSON 文件通常有 10-20 行
- `private_key` 字段特别长（有换行符 `\n`）
- 这是正常的，不用担心

### Q4: 服务账号邮箱格式是什么样的？

**格式**：
```
服务账号名称@项目ID.iam.gserviceaccount.com
```

**示例**：
```
twitter-bot-service@twitter-bot-123456.iam.gserviceaccount.com
```

---

## 📞 需要帮助？

如果某个步骤不清楚，请告诉我：
1. 你卡在哪一步？
2. 看到了什么界面？
3. 有没有错误提示？

我会提供更详细的指导！
