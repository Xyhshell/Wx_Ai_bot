# !/usr/bin/python3
# -*- coding:utf-8 -*-
# 先安装依赖
# pip3 install fastapi uvicorn python-multipart

# 主项目依赖
from flask import Flask, request
from threading import Thread
import os
import sys
import time
import json


from app import wx_main_

app = Flask(__name__)
app.config['SECRET_KEY'] = 'code 1024'


@app.route('/i', methods=('GET', 'POST'))
def hello():
    a = str(sys.executable)
    b = str(sys.argv)
    
    res = f"""
</br>Hello, World!
</br>运行解释器：{a}
</br>运行文件：{b}
"""

    return res


@app.route('/receive_msg', methods=['GET', 'POST'])
def print_json():
    if request.method == 'POST':
        data_content = request.form
        # print(data_content)

        sources = data_content['source']
        source = json.loads(sources)
        # print(type(source))
        # 发送人
        names = source["from"]["payload"]["name"]
        # print(names)

        content = data_content['content']
        # print(content)
        
        print(f"{names}: {content}")
        # 避免堵塞，使用线程
        Thread(target=wx_main_, args=(names, content, data_content)).start()
        
        # wx_main_(msg_content=str(content))
        # 处理接收到的POST请求数据
        return f"🚀{names}: Success"


if __name__ == '__main__':
    while True:
        app.run(host="0.0.0.0", port=3002, debug=True)
        time.sleep(3)
        os.execv(sys.executable, ['python'] + sys.argv)


