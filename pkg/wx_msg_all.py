import datetime
from time import sleep
import requests

from pkg.log import print_
# 全局变量
from pkg import glb_data


def push_wx_main(uh):
    """
    企业微信：推送异常检测
    :param uh:
    :return:
    """
    now_time = datetime.datetime.now()
    str_ti = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    ppush_url = f"{glb_data.myapi_push_url}/push?text={str_ti}\nlinux-chat Ai：{uh}！"
    print(requests.get(url=ppush_url))
    print_(f"#Chat Ai:{uh}")


# ----------------------------------------------------------------------
# 长文本限制!(字符长度）
text_len = 1600
#                          application/json
header = {'Content-Type': 'application/json'}


# 基本的文本消息
def wx_send_msg(send_, msg_):
    """
    推送消息给联系人，目前只支持文本消息
    :param send_:
    :param msg_:
    :return:
    """
    print(f"$用户:{send_}_|{msg_}")
    print_(f"$用户:{send_}|{msg_}")

    try:
        if len(msg_) > text_len:
            esult = [msg_[i: i + text_len] for i in range(0, len(msg_), text_len)]
            for ts_j in esult:
                print("###Root : 切割文本-->\n", ts_j)
                data_v2 = {
                    "to": f"{send_}",
                    "data": {"content": f"{ts_j}"}
                }
                print(data_v2)
                response_v2 = requests.post(glb_data.url_v2, json=data_v2, headers=header)
                print(response_v2.text)
                sleep(0.6)
        else:
            data_v2 = {
                "to": f"{send_}",
                "data": {"content": f"{msg_}"}
            }
            response_v2 = requests.post(glb_data.url_v2, json=data_v2, headers=header)
            print(response_v2.text)

    except Exception as e:
        print("### PUSH:", e)


# 媒体文件: 图片，音频
def wx_send_file(send_, file_path):
    """
    # 富文本，加强推送，应对ai消息的处理 !
    :param send_:
    :param file_path:
    :return:
    """

    print(f"User:>{send_}<")
    print_(f"$用户:{send_}|{file_path}")

    try:
        data_file = {
            "to": f"{send_}",
            "data": [{
                "type": "text",
                "content": f"{file_path}"
            }, {
                "type": "fileUrl",
                "content": f"{file_path}"
            }]}

        response_file = requests.post(glb_data.url_v2, json=data_file, headers=header)
        print(response_file.text)
    except Exception as e:
        print(e)
