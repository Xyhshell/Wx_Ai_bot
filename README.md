# Wx_Ai_bot（open users）

🀄 - linux wechat 的即时Ai信息处理脚本

## 基于[Linux-Wechat🚀](https://github.com/danni-cool/wechatbot-webhook)制作的Wechat-bot👨‍🎓
---

### 首先 感谢[原作者](https://github.com/danni-cool)对【Wechat for linux】的二次封装和docker支持

### **本项目依赖其部分特性，使用本项目前请配置好预置环境！**
> 🔵支持平台：Windows & Linux & MacOS

## 2024-03-22 - 所有优化在[V3版](https://github.com/Xyhshell/Wx_Ai_bot/tree/Wx_Ai_bot_V3)的基础上修改

### 写在前面：
🔝回复式文本处理脚本目前还在维护阶段，尚且存在不稳定情况。  
🔝私有化严重，[本项目](https://github.com/Xyhshell/Wx_Ai_bot/tree/Wx_Ai_bot_open_user)当前【03/22】定制化问题突出，不适合照搬搭建


### 删除：
1. ❌唯一用户限制
2. ❌冗余的片段
3. ❌无效函数
4. ❌本地文件缓存

### 更新：
1. ✅开放好友用户功能会话
2. ✅会话权限身份管理，限制好友用户使用管理员指令
3. ✅加入多用户管理，可以对会话用户实行白名单管理
4. ✅加入新AiChat，对话回复更精确
5. ✅加入日志功能，对所有用户的操作进行记录
6. ✅优化部分函数结构
7. ✅优化部分变量名
8. ✅优化逻辑处理
9. ✅优化部分指令模式

### 注意
1. 🔴全新的全局变量，在所有文件的 [ 配置脚本 ](https://github.com/Xyhshell/Wx_Ai_bot/blob/Wx_Ai_bot_open_user/pkg/glb_data.py) 需要的id,key,cookie等参数
2. 🔴由于最新版的通信接口变化，需要注意在推送api处配置自己的tokon
---

## 支持功能(默认无关键字对话，使用讯飞对接)

> **🔵Ai模型均是瀑布流式生成，文本较长时，回复反馈较慢 ❗**


### 管理员菜单
- @用户 ： 查看用户列表
- @添加 ： 添加✅白名单用户
- @删除 ： 删除❎白名单用户
- @si : 思知Robots + 
- @qy : 青云Robots +
- @jk ： 💪 +
- @ai ： 👩‍💻 +"""

### 普通用户菜单
 🐲《句应》: 支持关键字👍
- @help : 显示关键字菜单👨‍🎓
- @忘情水 : 🔥一句
- @句子 : 英📋汉句
- @笑话 : 添🐶日记
- @菜谱 ：做🍳方式 +
- @天气 ：查🌅状态 +
- @s : 讯飞文本🎊AI默认
- @t : 混元文本🚀模型
- @ps : 讯飞图片🌆(bate)
- @pt : 混元图片🌇(bate）
- @ca : ChatGpt(限额)"""
---
