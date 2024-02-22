import requests
from time import sleep

# # 插件
from pkg._wx_msg_all import *
from pkg import cityWeather
from pkg import H_app
from pkg import sfly
from pkg import txai


def wx_main_(name_, msg_content, data_content):
    """
    消息状态，轮询处理
    :param name_:
    :param msg_content:
    :return:
    """

    tianju = H_app.TianJu(t_name=name_)

    if msg_content == '@help':
        wx_send_msg(send_=name_, msg_=help_text)

    elif msg_content == '@忘情水':
        H_app.one(t_name=name_)

    elif "@句子" in msg_content:
        tianju.yinhanmingyan()

    elif "@笑话" in msg_content:
        tianju.tiangou()

    elif "@天气" in msg_content:
        b = msg_content.replace("@天气", "")
        wx_send_msg(send_=name_, msg_=f"开始查询：{b}")
        cityWeather.moji_weather(name_t=name_, city_=b)

    elif "@菜谱" in msg_content:
        e = msg_content.replace("@菜谱", "")
        tianju.caipu(key_word=e)

    elif "@s" in msg_content:
        s = msg_content.replace("@s", "")
        sfly.sf_word(s_name=name_, ides_=s)

    elif "@sp" in msg_content:
        sp = msg_content.replace("@sp", "")
        sfly.sf_pic(s_name=name_, ides_=sp)

    elif "@t" in msg_content:
        t = msg_content.replace("@t", "")
        txai.tx_msg(t_name=name_, tx_word=t)

    elif "@tp" in msg_content:
        tp = msg_content.replace("@tp", "")
        txai.tx_pic(t_name=name_, tx_pic_=tp)

    # old
    # todo:后续四个慢回复bot
    elif "@si" in msg_content:
        c = msg_content.replace("@si", "")
        H_app.sizhi(t_name=name_, sizi_word=c)

    elif "@qy" in msg_content:
        d = msg_content.replace("@qy", "")
        H_app.qingyunke(t_name=name_, qy_word=d)

    elif "@jk" in msg_content:
        f = msg_content.replace("@jk", "")
        tianju.jiankang(jk_word=f)

    elif "@ai" in msg_content:
        g = msg_content.replace("@ai", "")
        tianju.robot(question=g)

    else:
        # 暂时接替空任务对话
        print(f"💨{data_content}👌")
        txai.tx_msg(t_name=name_, tx_word=msg_content)
        # wx_send_msg("空指令 / 无意义消息！")


help_text = """🐲: 支持关键字👍
@忘情水 : 🔥一句
@句子 : 英📋汉句
@笑话 : 添🐶日记
- @天气 ：查🌅状态 +
- @菜谱 ：做🍳方式 +
- @s : 讯飞星火🎊AI(文本消息)
- @sp : 讯飞星火🌆AI(图片生成)
- @t : 腾讯🚀混元模型(文本）
- @tp : 腾讯🌇混元模型(图片）
- @sz : 思知Robots + 
- @qy : 青云Robots +
- @jk ： 💪 +
- @ai ： 👩‍💻 +
"""

# 启动延时
sleep(36)
wx_send_msg(send_="忄", msg_=help_text)


