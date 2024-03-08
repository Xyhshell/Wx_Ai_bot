# 内部推送
from pkg._wx_msg_all import *
# 插件
from pkg import cityWeather
from pkg import H_app
from pkg import sfly
from pkg import txai


def wx_main_(name_, msg_content, data_content):
    """
    消息状态，轮询处理
    :param data_content: # 接受的所有Key值数据
    :param name_:
    :param msg_content:
    :return:
    """

    tianju = H_app.TianJu(t_name=name_)

    if msg_content != "":
        wx_send_msg(send_=name_, msg_=f"$ 开始处理:\n{msg_content}")
        sleep(0.3)

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
            print(f"\n\n{data_content}\n👌\n")
            # 进入讯飞Ai
            sfly.sf_word(s_name=name_, ides_=msg_content)


# docker - chat 检测  todo: docker wechat bot :3001
urls = "http://127.0.0.1:3001/healthz?token=【tokon】"

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
- @ai ： 👩‍💻 +"""


def info_():
    while True:
        try:
            r1 = requests.get(urls).text
            if r1 == "healthy":
                break
            else:
                sleep(3)
        except Exception as e:
            push_wx_main(uh=e)
            sleep(3)
    try:
        # 仅发送管理员 ：todo: 微信昵称
        wx_send_msg(send_="#", msg_=help_text)
    except Exception as e:
        push_wx_main(uh=e)
        info_()
