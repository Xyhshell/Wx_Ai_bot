import re
from sparkdesk_web.core import SparkWeb

from pkg.wx_msg_all import *
# 全局变量
from pkg import glb_data

# 请根据自己配置三个参数
sparkWeb = SparkWeb(
    cookie=glb_data.sf_cookie,
    fd=glb_data.sf_fd,
    GtToken=glb_data.sf_GtToken
)

chat = sparkWeb.create_continuous_chat()


# 讯飞星火主接口
def sf_word(s_name, ides_):
    """
    主要进行文本处理
    :param s_name:
    :param ides_:
    :return:
    """
    sf_req = chat.chat(str(ides_))
    print("SF文本处理:\n", sf_req)
    wx_send_msg(send_=s_name, msg_=sf_req)


def sf_pic(s_name, ides_):
    """
    绘画处理
    :param s_name:
    :param ides_:
    :return:
    """
    sf_req_pic = chat.chat(str(ides_))
    print("SF图片处理:\n", sf_req_pic)
    sf_pic_url = re.findall(':"(.*?)"}', sf_req_pic, flags=re.DOTALL)[0]
    sleep(0.1)
    wx_send_file(send_=s_name, file_path=sf_pic_url)
