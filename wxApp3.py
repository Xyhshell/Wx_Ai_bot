# !/usr/bin/python3
# -*- coding:utf-8 -*-
# 先安装依赖
# pip3 install fastapi uvicorn python-multipart
#
# http://100.66.10.10:3001/login?token=jingmoshell
# http://100.66.10.10:3001/healthz?token=jingmoshell
#
# 主项目依赖
from time import sleep

import requests
from flask import Flask, request, Response
from threading import Thread
import sys
import json

from pkg._wx_msg_all import push_wx_main
from wx_lib import wx_main_, info_

app = Flask(__name__)
app.config['SECRET_KEY'] = 'code 1024'


@app.route('/i', methods=('GET', 'POST'))
def hello():
    a = str(sys.executable)
    b = str(sys.argv)

    res = f"""
</br>Hello, World!
</br>
</br>运行解释器：{a}
</br>运行文件：{b}
"""

    return res


@app.route('/msg', methods=['POST'])
def print_json():
    if request.method == 'POST':
        # 所有返回值信息
        data_content = request.form
        print(data_content)

        sources = data_content['source']
        source = json.loads(sources)
        print(type(source))
        # 发送人
        names = source["from"]["payload"]["name"]
        print(names)

        content = data_content['content']
        print(content)

        print(f"{names}: {content}")
        # 避免堵塞，使用线程
        Thread(target=wx_main_, args=(names, content, data_content)).start()

        return Response(json.dumps(source), mimetype='application/json')


def keep_():
    try:
        # 上线即推送 help 消息 | 已做异常处理
        info_()

        # 启动flask todo: 自定义host地址
        app.run(host="127.0.0.1", port=3002, debug=False)

    except Exception as e:
        push_wx_main(uh=e)
        sleep(3)
        keep_()


if __name__ == '__main__':
    keep_()
