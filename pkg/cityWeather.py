#!/usr/bin/python
# -*- coding:utf-8 -*-
# @FileName  :moji_weather.py
# @Time      :2020/09/21 19:44

import json
from lxml import etree

import requests
from time import sleep

try:
    from pkg._wx_msg_all import *
except ImportError:
    from _wx_msg_all import *


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/79.0.3945.29 Safari/537.36 Edg/79.0.309.18 "
}


def start():
    with open('./today.txt', "r", encoding='utf-8') as f:  # 设置文件对象
        text_all = f.read()  # 可以是随便对文件的操作
    # print(text_all)
    return text_all


def download(txt):
    with open('./today.txt', 'a', encoding='utf-8') as f:
        f.write(str(txt))


def weather(cityid_):
    city_idurl = f"https://tianqi.moji.com/api/redirect/{cityid_}"

    weather_city = requests.get(city_idurl, headers=headers)
    weather_city.encoding = weather_city.apparent_encoding
    html = etree.HTML(weather_city.text)

    with open('./today.txt', 'w', encoding='utf-8') as f:
        f.write('')

    adder = html.xpath('//*[@id="search"]/div[1]/div[1]/em//text()')
    for y in adder:
        if "\n" in y:
            pass
        else:
            t10 = '当前定位地址:\n %5s' % y
            download(t10)

    weather_01 = html.xpath('/html/body/div[4]/div[1]/div[1]//text()')
    for q in weather_01:
        if "\n" in q:
            pass
        else:
            t2 = '\n空气质量:%5s' % q
            download(t2)

    weather_02 = html.xpath('/html/body/div[4]/div[1]/div[2]//text()')
    t3 = '\r今日气温:'
    download(t3)
    for w in weather_02:
        if "\n" in w:
            pass
        else:
            t4 = '%3s  ' % w
            download(t4)

    for d in range(3, 5):
        weather_03 = html.xpath(f'/html/body/div[4]/div[1]/div[{d}]//text()')
        for h in weather_03:
            if "\n" in h:
                pass
            else:
                t5 = '\n%5s' % h
                download(t5)
        t6 = ""
        download(t6)

    t7 = '\n\nTips:未来天气预告\n\n'
    download(t7)

    for i in range(1, 4):
        weather_04 = html.xpath(f'/html/body/div[5]/div[1]/div[1]/ul[{i}]//text()')

        pr = (weather_04[2], weather_04[8], weather_04[10], weather_04[13], weather_04[15])

        for line in pr:
            odom = line.split()
            tmp_str = " ".join(odom)
            result = ' '.join(tmp_str.split('='))
            t9 = "%5s " % result
            download(t9)
        t11 = '\n'
        download(t11)


def main_city_id(name_, city_):
    # city_ = input("City:—>")
    try:
        search_url = f"https://tianqi.moji.com/api/citysearch/{city_}"
        r = requests.get(search_url, headers=headers)

        r.encoding = r.apparent_encoding
        # print(type(r))
        # print(r.text)
        # print()
        dict_ = json.loads(r.text)
        # print(type(dict_))
        # print(dict_)
        # print(dict_["city_list"][0]["cityId"])
        send_id = dict_["city_list"][0]["cityId"]
        return send_id
    except:
        wx_send_msg(send_=name_, msg_="错误！核实是否为县市区")


def moji_weather(name_t, city_):
    cityid = main_city_id(name_=name_t, city_=city_)
    weather(cityid_=cityid)
    wx_send_msg(send_=name_t, msg_=start())
    # print(start())
















