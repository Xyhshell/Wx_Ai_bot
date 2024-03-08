import requests
import datetime
from time import sleep

"""
主要作用的监控微信的在线状态，掉登录今后进行告警
"""

urls = "http://127.0.0.1:3001/healthz?token=【tokon】"


def push_wx(uh):
    now_time = datetime.datetime.now()
    str_ti = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    # 自搭建的一个服务随送接口 todo: 可以删除，也可以自行搭建保留，目的是监控微信的登录状态
    ppush_url = f"http://127.0.0.1:9001/push?text={str_ti}\nlinux-chat 状态：{uh}！"
    print(requests.get(url=ppush_url))
    sleep(6)


def stop_if():
    k = 1
    while True:
        o = is_or()
        if o == "unHealthy":
            if k == 1:
                print("下线", o)
                push_wx(uh=o)
                k = 0
                continue
            else:
                print("s 状态恒定：", o)
                sleep(60 * 30)
                continue

        if o == "healthy":
            print("在线")
            push_wx(uh=o)
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
                push_wx(uh=i)
                t = 0
                continue
            else:
                print("a 状态恒定：", i)
                sleep(60 * 30)
                continue

        if i == "unHealthy":
            print("下线")
            push_wx(uh=i)
            t = 1
            stop_if()
            continue


def is_or():
    try:
        r1 = requests.get(urls)
        fg = r1.text
        return fg
    except Exception as e:
        push_wx(uh=e)
        sleep(6)
        always_if()


if __name__ == '__main__':
    sleep(10)
    print(requests.get(url="http://100.66.10.10:9001/push?text=linux-chat 状态：wx_info 开始检测..."))
    always_if()

