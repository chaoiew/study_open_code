# OpenCode 高效沟通指南

## 1. 基础原则

| ❌ 低效表达 | ✅ 高效表达 |
|------------|------------|
| "帮我看看这个代码" | "Find the bug in `/src/api/auth.ts` - login returns 500" |
| "优化一下这个项目" | "Add connection pooling to the database layer - current setup creates new connection per request" |
| "实现登录功能" | "Implement JWT auth with httpOnly cookies for `/api/auth/*` routes" |

## 2. Message 结构模板

```markdown
## 目标
[一句话说明你要做什么]

## 上下文
[相关文件路径、当前问题]
- file: src/users/user.ts (line 45 breaks)

## 约束
[技术栈、限制条件]
- 只能用 Python 3.11+
- 不能新增依赖

## 期望结果
[成功标准]
- 登录后 token 存储在 httpOnly cookie
- 过期时间 7 天
```

## 3. Story.md 写法

```markdown
## User Story
作为 [角色]，我想 [功能]，以便 [收益]

## Acceptance Criteria
- [ ] AC1: 用户输入有效邮箱显示成功
- [ ] AC2: 用户输入无效邮箱显示错误 "Invalid email format"
- [ ] AC3: 提交后 loading 状态 500ms

## Technical Notes
- 涉及文件: `src/forms/EmailForm.tsx`
- 依赖: `zod` 验证
- 不要修改: API 层
```

## 4. 场景示例

| 场景 | 推荐问法 |
|-----|---------|
| **调试** | "Line 42 in `auth.ts` throws `TypeError: Cannot read property 'id'` - attach relevant code snippet" |
| **实现** | "Add rate limiting to `/api/users` using in-memory store, max 100 req/min per IP" |
| **重构** | "Extract `validateEmail()` from `utils.ts` to `src/validation/email.ts` - keep existing tests passing" |
| **研究** | "How does the current auth flow work in `src/auth/`? Find the entry point and token validation logic" |

## 5. 关键技巧

1. **给文件路径** - 我可以直接读，比你说"那个登录文件"快
2. **给错误信息** - 直接贴 stack trace，比描述"报错了"快 10 倍
3. **明确范围** - 说"只改 A，不要动 B"，比"帮我优化一下"有用
4. **说目标而非过程** - "我要实现分页" 而不是 "在 Controller 里加个 limit 参数"

## 6. 不要做的事

- ❌ "帮我看看" / "Look into this" → 给具体路径或错误
- ❌ 一次问 5 个不相关问题 → 分开问
- ❌ 只给文件不说话 → 加一句你想做什么
- ❌ "怎么做" → 问我实现还是给方案让我选

## 7. 更多进阶技巧

### 链式小任务
把 2-3 个相关改动放一个请求，token 更省：

```
"in aa.py: rename f() to add(), update call on line 8, update aa.md"
```

### 提供期望 vs 实际
调试时展示预期结果：

```
"f(1,2) 返回 3 但应该返回 4"
```

### 约束前置
偏好只说一次：

```
"只改 aa.py，不要动测试，遵循现有风格"
```

### 满意时说 "done"
避免不必要的后续建议。

### 利用会话上下文
之前说过的不用重复，只补充当前步骤需要的信息。
