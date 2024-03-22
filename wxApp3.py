# !/usr/bin/python3
# -*- coding:utf-8 -*-
# 先安装依赖
#
import os
import time
# 主项目依赖
from time import sleep
from flask import Flask, request, Response
from threading import Thread
import sys
import json

from wx_lib import info_, AdminMian
# 全局变量
from pkg import glb_data
# 部分模块
from pkg.wx_msg_all import push_wx_main
from pkg.log import print_

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jingmoshell, jingmo code 1024'


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

        # 包含的文本信息
        content = data_content['content']
        # 发送人
        names = source["from"]["payload"]["name"]

        # 类形判断，一般为str
        if type(content) is str or int:
            post_main = AdminMian(name_=names, msg_content=content)
            print(f"{names}: {content}")
            print_(f"{names}: {content}")
            # 避免堵塞，使用线程  # 处理接收到的POST请求数据
            Thread(target=post_main.user_main, args=()).start()

        else:
            print_(f"# 用户：{names}发送消息！非文本被驳回！")

        return Response(json.dumps(source), mimetype='application/json')


def keep_():
    try:
        # 上线即推送 help 消息 | 已做异常处理
        info_()
        # 启动flask
        app.run(host=glb_data.host, port=glb_data.port, debug=False)

        # while True:
        #     app.run(host=glb_data.host, port=glb_data.port, debug=True)
        #     time.sleep(3)
        #     os.execv(sys.executable, ['python'] + sys.argv)

    except Exception as e:
        push_wx_main(uh=e)
        sleep(3)
        keep_()


if __name__ == '__main__':
    keep_()
