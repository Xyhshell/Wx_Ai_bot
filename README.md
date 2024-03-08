# Wx_Ai_bot

linux wechat的即时Ai信息处理脚本

# 基于[Linux-Wechat🚀](https://github.com/danni-cool/wechatbot-webhook)制作的Wechat-bot👨‍🎓

---

## 首先 感谢[原作者](https://github.com/danni-cool)对【Wechat for linux】的二次封装和docker支持的，才有的本项目的诞生！

---



# 2024-03-09

### 更新：
1. 优化部分变量名
2. 优化逻辑处理
3. 加入对话反馈处理
4. 新增登录状态监测
5. 加入部分异常告警推送

### 文件配置：
* 在所有需要注意的地方均已经添加【TODO】标识，请参照教程，配置各项参数。
* 由于最新版的通信接口变化，需要注意在推送api处配置自己的tokon


### 实现原理 和 二改

> - 基于原项目的一些收发接口的实现，本项目在对消息处理上进行判断和二次封装!
> - 对接 [讯飞星火](https://xinghuo.xfyun.cn/) 和 [腾讯混元大模型](https://hunyuan.tencent.com/), 实现AI文字处理能力和图片生成能力。
> - 加入一些其他能力（具体看源码）

> - 支持平台：Windows & linux
>   > 未测 Mac

---

## 支持功能(默认无关键字对话，使用腾讯混元对接)

> **ai模型均是瀑布流式打印，文本生成较长时，可能反馈较慢**

- 🐲: 支持关键字👍
- ~~@ip : QG的docker-ip😘~~
- @忘情水 : 🔥一句
- @句子 : 英📋汉句
- @笑话 : 添🐶日记
- @天气 ：查🌅状态 +
- @菜谱 ：做🍳方式 +
- @s : 讯飞星火cookie文本消息)
- @sp : 讯飞星火🌆AI(图片生成)
- @t : 腾讯🚀混元模型(文本）
- @tp : 腾讯🌇混元模型(图片）
- @sz : 思知Robots +
- @qy : 青云Robots +
- @jk ： 💪 +
- @ai ： 👩‍💻 +

---

## 配置 : key cookie

* 各项需要留意的片段 **在Pycharm中** 已经用 **todo** 标注

## 参考：

* 混元：https://github.com/HarcicYang/rev_HunYuan

* 讯飞文档：https://github.com/HildaM/sparkdesk-api/tree/main/docs

* 星火：https://github.com/HildaM/sparkdesk-api

* 天聚数行：https://www.tianapi.com/console/

---
## **声明：本项目只分享思路，未经许可，禁止商用！**
---
