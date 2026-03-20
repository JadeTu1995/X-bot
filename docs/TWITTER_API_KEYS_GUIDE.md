# 🔑 Twitter API 密钥获取完整指南

## 📋 你已经找到的密钥

✅ **Consumer Key**（也叫 API Key）
✅ **Secret Key**（也叫 API Key Secret）
✅ **Bearer Token**

## ⚠️ 还需要的密钥

❌ **Access Token**
❌ **Access Token Secret**

---

## 🎯 目标：获取 Access Token 和 Access Token Secret

### 步骤 1：进入 Twitter 开发者门户

1. 访问：https://developer.twitter.com/en/portal/dashboard
2. 确保你已经登录 Twitter 账号

### 步骤 2：找到你的应用

1. 点击左侧菜单的 **"Projects & Apps"**
2. 你应该能看到一个项目和应用的列表
3. 点击你的应用名称（通常是类似 "paper-bot" 这样的名字）

### 步骤 3：设置正确的权限 ⚠️ 非常重要

在生成 Access Token 之前，**必须先设置正确的权限**！

1. 点击应用后，进入 **"Settings"** 标签页
2. 向下滚动，找到 **"User authentication settings"** 部分
3. 点击 **"Set up"** 按钮

4. 在弹出的页面中：
   - **Permissions**：选择 **"Read and Write"**（读写权限）
   - **Type of App**：选择 **"Web App, Automated App or Bot"**
   
5. 点击 **"Save"** 保存

**⚠️ 注意**：如果你之前已经设置过权限，请确认是"Read and Write"，而不是"Read Only"。

### 步骤 4：生成 Access Token

1. 回到应用的 **"Keys and Tokens"** 标签页
2. 向下滚动，找到 **"Access Token and Secret"** 部分
3. 点击 **"Generate"** 按钮（如果已经生成过，会显示 "Regenerate"）

4. 系统会显示两个新的密钥：
   - **Access Token**：类似 `123456789-AbCdEfGhIjKlMnOpQrStUvWxYz`
   - **Access Token Secret**：类似 `AbCdEfGhIjKlMnOpQrStUvWxYz1234567890`

5. **⚠️ 重要**：立即复制并保存这两个密钥！
   - 关闭后无法再次查看
   - 如果忘记了，需要重新生成

---

## 📝 完整的密钥清单

请确认你已经复制并保存了以下 **5 个密钥**：

### 1. Consumer Key（API Key）
- **在 Twitter 开发者门户叫**：`API Key` 或 `Consumer Key`
- **在 GitHub Secrets 叫**：`TWITTER_API_KEY`
- **格式示例**：`AbCdEfGhIjKlMnOpQrStUvWx`

**你的值**：`_______________________________`

### 2. Consumer Secret（API Key Secret）
- **在 Twitter 开发者门户叫**：`API Key Secret` 或 `Consumer Secret`
- **在 GitHub Secrets 叫**：`TWITTER_API_SECRET`
- **格式示例**：`AbCdEfGhIjKlMnOpQrStUvWxYz1234567890`

**你的值**：`_______________________________`

### 3. Access Token
- **在 Twitter 开发者门户叫**：`Access Token`
- **在 GitHub Secrets 叫**：`TWITTER_ACCESS_TOKEN`
- **格式示例**：`123456789-AbCdEfGhIjKlMnOpQrStUvWxYz`

**你的值**：`_______________________________`

### 4. Access Token Secret
- **在 Twitter 开发者门户叫**：`Access Token Secret`
- **在 GitHub Secrets 叫**：`TWITTER_ACCESS_TOKEN_SECRET`
- **格式示例**：`AbCdEfGhIjKlMnOpQrStUvWxYz1234567890`

**你的值**：`_______________________________`

### 5. Bearer Token（可选）
- 这个密钥在这个项目中暂时不需要
- 如果你看到了，可以保存备用

**你的值**：`_______________________________`

---

## 🎯 对照关系表

| Twitter 开发者门户的名称 | GitHub Secrets 名称 | 说明 |
|----------------------|-------------------|------|
| API Key | TWITTER_API_KEY | ✅ 你已经找到 |
| API Key Secret | TWITTER_API_SECRET | ✅ 你已经找到 |
| Access Token | TWITTER_ACCESS_TOKEN | ❌ 还需要生成 |
| Access Token Secret | TWITTER_ACCESS_TOKEN_SECRET | ❌ 还需要生成 |

---

## ⚠️ 常见问题

### Q1: 我找不到 "Generate" 按钮？

**可能原因**：
- 你还没有设置权限为 "Read and Write"
- 或者已经生成过了（会显示 "Regenerate"）

**解决方法**：
1. 先去 Settings 设置权限为 "Read and Write"
2. 回到 "Keys and Tokens" 标签
3. 应该能看到 "Generate" 或 "Regenerate" 按钮

### Q2: 我之前生成过 Access Token，还有效吗？

**检查方法**：
- 如果权限是 "Read and Write"，那么有效
- 如果权限是 "Read Only"，需要重新生成

**建议**：
- 点击 "Regenerate" 重新生成，确保是最新的

### Q3: 点击 "Generate" 后显示的密钥我没有保存，怎么办？

**解决方法**：
- 无法再次查看，只能重新生成
- 点击 "Regenerate" 按钮重新生成新的密钥

### Q4: Access Token 的格式是什么样的？

**Access Token 格式**：
- 通常以数字开头，然后是横线，然后是字母和数字
- 示例：`123456789-AbCdEfGhIjKlMnOpQrStUvWxYz`

**Access Token Secret 格式**：
- 纯字母和数字组合
- 示例：`AbCdEfGhIjKlMnOpQrStUvWxYz1234567890`

---

## 🎯 下一步：配置 GitHub Secrets

当你获取到所有 4 个密钥后，就可以配置 GitHub Secrets 了：

1. **打开 GitHub 仓库**
   - 进入你的仓库页面

2. **进入设置**
   - 点击 "Settings" 标签
   - 左侧菜单选择 "Secrets and variables" > "Actions"

3. **添加以下 4 个 Secrets**：

   ```
   Name: TWITTER_API_KEY
   Value: [粘贴你的 API Key]
   ```

   ```
   Name: TWITTER_API_SECRET
   Value: [粘贴你的 API Key Secret]
   ```

   ```
   Name: TWITTER_ACCESS_TOKEN
   Value: [粘贴你的 Access Token]
   ```

   ```
   Name: TWITTER_ACCESS_TOKEN_SECRET
   Value: [粘贴你的 Access Token Secret]
   ```

---

## ✅ 检查清单

请确认以下所有项目：

- [ ] 我已经找到了 API Key（Consumer Key）
- [ ] 我已经找到了 API Key Secret（Consumer Secret）
- [ ] 我已经在 Twitter 开发者门户设置了 "Read and Write" 权限
- [ ] 我已经生成了 Access Token
- [ ] 我已经生成了 Access Token Secret
- [ ] 我已经保存了所有 4 个密钥

---

## 📞 如果还有问题

如果按照这个指南还是找不到，请告诉我：
1. 你现在在 Twitter 开发者门户的哪个页面？
2. 你看到了什么按钮或选项？
3. 有没有截图可以分享？

我会帮你一步步解决！
