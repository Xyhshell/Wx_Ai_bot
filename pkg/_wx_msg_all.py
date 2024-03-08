from time import sleep
import requests


def push_wx_main(uh):
    """
    企业微信：推送异常检测
    :param uh:
    :return:
    """
    # todo: 搭建的全局告警接口
    ppush_url = f"http://127.0.0.1:9001/push?text=Chat Ai：\n{uh}！"
    print(requests.get(url=ppush_url))


# ----------------------------------------------------------------------
# 长文本限制!(字符长度）
text_len = 1600
# 传送的内部接口 v2版 ：https://github.com/danni-cool/wechatbot-webhook
# 暂定最新版需要tokon 验证消息
#         http://127.0.0.1:3001/webhook/msg/v2?token=}
# todo: 最新版需要验证，推送接口需要加上 自己的 tokon
url_v2 = "http://127.0.0.1:3001/webhook/msg/v2?token="
#                           application/json
headers = {'Content-Type': 'application/json'}


# 基本的文本消息
def wx_send_msg(send_, msg_):
    """
    推送消息给联系人，目前只支持文本消息
    :param send_:
    :param msg_:
    :return:
    """
    print(f"User:>{send_}<")

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
                response_v2 = requests.post(url_v2, json=data_v2, headers=headers)
                print(response_v2.text)
                sleep(0.6)
        else:
            data_v2 = {
                "to": f"{send_}",
                "data": {"content": f"{msg_}"}
            }
            response_v2 = requests.post(url_v2, json=data_v2, headers=headers)
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

        response_file = requests.post(url_v2, json=data_file, headers=headers)
        print(response_file.text)
    except Exception as e:
        print(e)
