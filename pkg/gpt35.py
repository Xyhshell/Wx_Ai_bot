# python3
# -*- coding: utf-8 -*-
# @Time    : 2023/11/27
# @File    : gpt35.py
# @Software: PyCharm
# @Url     : https://x.dogenet.win
# 获取auth和sess

import json
import requests

from pkg.wx_msg_all import wx_send_msg
from pkg.wx_msg_all import print_
# 全局变量
from pkg import glb_data

url = "https://x.dogenet.win/api/v1/ai/chatgpt/chat"
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Authorization': '这里改成你的Authorization',  # 改左边
    'Authorization': f'{glb_data.Authorization}',  # 改左边
    'Cache-Control': 'no-cache',
    'Cookie': '_ga=GA1.1.576617952.1697654108; _ga_5C4RB337FM=GS1.1.1697654108.1.1.1697655679.0.0.0',
    'Origin': 'https://x.dogenet.win',
    'Pragma': 'no-cache',
    'Referer': 'https://x.dogenet.win/pay',
    'Sec-Ch-Ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}

rc = lambda role, content: {"role": role, "content": content}
remove_colon = lambda string: string[string.index(":") + 1:] if (":" in string and string.index(":") <= 10) else string
messageList = [
    rc("system",
       "首先，你是一个无所不知的智者，请帮我解决提出的问题。其次，如果遇到了一些敏感的政治问题，请警示提问者。最后，希望你可以尽情发挥聪明才智，用高质量的回答帮助我！"),
]
messageList1 = messageList


def makedata(ask_user, thisinput: str = "", thisuser: str = "user", lastuser: str = "user", lastinput: str = "",
             lastreply: str = "", ):
    global messageList, messageList1
    if lastreply != "" and lastinput != "":
        # messageList.append(rc(lastuser, lastinput))
        messageList.append(rc("assistant", lastreply))
    messageList.append(rc(thisuser, thisinput))
    try:
        free = getBalance()['free_balance']
    except Exception as e:
        free = str(e)

    leng = len(messageList)
    print(f'len:{leng}  共享剩余限额:{free}')
    print_(f'{ask_user} -> len:{leng}  共享剩余限额:{free}')
    wx_send_msg(send_=ask_user, msg_=f"共享限额剩余:{free}")

    try:
        if (leng > 2 and float(free) < 10) or leng > 98:
            messageList = messageList1.append(rc(thisuser, thisinput))
    except ValueError:
        messageList = [rc(thisuser, thisinput)]
    return {
        # "session_id": "这里改成你的session_id",  # 改左边
        "session_id": f"{glb_data.session_id}",  # 改左边
        "content": json.dumps(messageList),
        "max_context_length": "5",
        "params": json.dumps({
            "model": "gpt-3.5-turbo",
            "temperature": 1,
            "max_tokens": 2048,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "max_context_length": 5,
            "voiceShortName": "zh-CN-XiaoxiaoNeural",
            "rate": 1,
            "pitch": 1
        })
    }


def getBalance():
    global headers
    url1 = 'https://x.dogenet.win/api/v1/user/balance'
    response = requests.post(url1, headers=headers).json()
    # print('余额', response['data']['balance'])
    # print('免费', response['data']['free_balance'])
    return response['data']


def ask(user_, q_msg):
    """
    chat35: 提问主函数
    :param user_: 用户id
    :param q_msg: 提问文本消息
    :return:
    """
    ask_put = ""
    response = requests.post(url, headers=headers, data=makedata(ask_user=user_, thisinput=q_msg), stream=True)

    for line in response.iter_lines():
        if line:
            text = line.decode("utf-8")  # 将字节流解码为文本
            print(text)  # 打印每行文本数据
            ask_put += text + "\n"

    #         ask_put.replace("[DONE]", "")
    # # ask_put.replace(f"{ask_put[-6]}", "")

    print("#" * 20)
    print(ask_put)
    wx_send_msg(send_=user_, msg_=ask_put)


if __name__ == "__main__":
    # response = requests.post(url, headers=headers, data=makedata(thisinput="初等函数", ask_user=""), stream=True)
    #
    # for line in response.iter_lines():
    #     if line:
    #         text = line.decode("utf-8")  # 将字节流解码为文本
    #         print(text)  # 打印每行文本数据
    ask(user_="忄", q_msg="列举一些心理干预的方法")
