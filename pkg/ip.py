import time
import requests
from lxml import etree

# 全局变量
from pkg import glb_data

data = {
    'login': glb_data.cpolar_login,
    'password': glb_data.cpolar_password,
    "csrf_token": glb_data.cpolar_csrf_token,
}

login_url = 'https://dashboard.cpolar.com/login'
status_url = "https://dashboard.cpolar.com/status"


def getip():
    session = requests.session()
    session.post(url=login_url, data=data, headers=glb_data.headers)
    time.sleep(0.6)
    res = session.get(url=status_url, headers=glb_data.headers)
    res.encoding = res.apparent_encoding
    html = etree.HTML(res.text)

    texts = ""
    try:
        url_name = html.xpath('//tbody/tr/td[1]//text()')
        url_th = html.xpath('//tbody/tr/th//text()')
        # url_local = html.xpath('//tbody/tr/td[3]//text()')
        url_time = html.xpath('//tbody/tr/td[4]//text()')

        list_len = len(url_name)
        for i in range(0, list_len):
            text = f"""💐：jingmo\n🎯{url_name[i]}: {url_time[i].split(" +")[0]}✨\nLink: {url_th[i]}\n"""
            texts += text
        print(texts)

        return texts

    except Exception as e:
        print("> 获取发生错误！即将重新探测...", e)
        time.sleep(3)
        getip()
