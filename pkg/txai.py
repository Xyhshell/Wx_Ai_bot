from rev_HunYuan import *

try:
    from pkg._wx_msg_all import *
except ImportError:
    from _wx_msg_all import *

# .replace(old_str, new_str)


bot = HunYuan(
    # todo: 参照教程，获取cookie
    cookie="b-user-id="
)


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


# tx_pic(tx_pic_="帮我画一幅山水画")
# {"text": "你好，有什么我可以帮助你的吗？", "images": []}
# {"text": "这是一条图片信息", "images": [{"highImgUrl": imgUrlHigh, "lowImgUrl": imgUrlLow}, {"highImgUrl": imgUrlHigh, "lowImgUrl": imgUrlLow}, {"highImgUrl": imgUrlHigh, "lowImgUrl": imgUrlLow}]}
