import requests
from time import sleep

from pkg import wx_msg_all

# 全局变量
from pkg import glb_data


def stop_if():
    k = 1
    while True:
        o = is_or()
        if o == "unHealthy":
            if k == 1:
                print("下线", o)
                wx_msg_all.push_wx_main(uh=o)
                sleep(6)
                k = 0
                continue
            else:
                print("s 状态恒定：", o)
                sleep(60 * 15)
                continue

        if o == "healthy":
            print("在线")
            wx_msg_all.push_wx_main(uh=o)
            sleep(6)
            k = 1
            always_if()
            continue


def always_if():
    t = 1
    while True:
        i = is_or()
        if i == "healthy":
            if t == 1:
                print("在线", i)
                wx_msg_all.push_wx_main(uh=i)
                sleep(6)
                t = 0
                continue
            else:
                print("a 状态恒定：", i)
                sleep(60 * 15)
                continue

        if i == "unHealthy":
            print("下线")
            wx_msg_all.push_wx_main(uh=i)
            sleep(6)
            t = 1
            stop_if()
            continue


def is_or():
    try:
        r1 = requests.get(glb_data.mychat_url)
        fg = r1.text
        return fg
    except Exception as e:
        wx_msg_all.push_wx_main(uh=e)
        sleep(6)
        always_if()


if __name__ == '__main__':
    sleep(15)
    print(requests.get(url=f"{glb_data.myapi_push_url}/push?text=linux-chat 状态：wx_info 开始检测..."))
    always_if()
