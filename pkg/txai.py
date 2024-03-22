from rev_HunYuan import *

from pkg.wx_msg_all import *
# 全局变量
from pkg import glb_data

# .replace(old_str, new_str)
bot = HunYuan(cookie=glb_data.tx_cookie)


def tx_msg(t_name, tx_word):
    result = bot.ask(prompt=f"{tx_word}",  # 要发送的内容
                     model="gpt_175B_0404"  # 使用的模型，一般无需填写
                     )
    print(type(result))
    print(result)
    tx_req = result["text"].replace("\u200d", " ")
    wx_send_msg(send_=t_name, msg_=tx_req)
    # print(tx_req)


def tx_pic(t_name, tx_pic_):
    result_pic = bot.ask(prompt=f"{tx_pic_}",  # 要发送的内容
                         model="gpt_175B_0404"  # 使用的模型，一般无需填写
                         )
    print(type(result_pic))
    tx_pic_req = result_pic["images"][0]["highImgUrl"]
    # print(tx_pic_req)
    wx_send_file(send_=t_name, file_path=tx_pic_req)

