import json

from pkg.wx_msg_all import *
# 全局变量
from pkg import glb_data


def one(t_name):
    """
    获取一条一言。
    :return:
    """
    url = "https://v1.hitokoto.cn/"
    res = requests.get(url).json()
    text_res = res["hitokoto"] + "     ——" + res["from"]
    wx_send_msg(send_=t_name, msg_=text_res)


# 思知机器人 智障
def sizhi(t_name, sizi_word: str):
    sess = requests.get(f'https://api.ownthink.com/bot?spoken={sizi_word}', headers=glb_data.headers)
    answer = sess.text
    answer = json.loads(answer)["data"]["info"]["text"]
    wx_send_msg(send_=t_name, msg_=answer)
    print(answer)


# 青云机器人 简单对话
def qingyunke(t_name, qy_word: str):
    qy_url = f"http://api.qingyunke.com/api.php?key=free&appid=0&msg={qy_word}"
    qy_req = requests.get(qy_url, headers=glb_data.headers)
    qy_text = json.loads(qy_req.text)["content"]

    wx_send_msg(send_=t_name, msg_=qy_text)
    print(qy_text)


# 天聚 部分Api
class TianJu:
    def __init__(self, t_name):
        self.key = glb_data.tianju_key
        self.t_name = t_name

    def caidan_moudl(self, cp_name, zuofa, texing, tishi, tiaoliao, yuanliao):
        """
        菜谱推送模板
        :return:
        """
        caipu_msg = f"""【菜名】：{cp_name}
【做法】{zuofa}
【特征】{texing}
【留意】{tishi}
【调料】{tiaoliao}
【原料】{yuanliao}"""

        wx_send_msg(send_=self.t_name, msg_=caipu_msg)

    # 菜谱
    def caipu(self, key_word):
        cp_url = "https://apis.tianapi.com/caipu/index"
        data_ = {
            "key": self.key,
            "word": key_word,
            "num": 3,
            "page": 1
        }
        caipu_req = requests.post(url=cp_url, data=data_).json()

        if caipu_req["code"] == 200:
            caipu_info = f"""食材："{key_word}"\n状态：菜谱🥘{caipu_req["msg"]}"""
            wx_send_msg(send_=self.t_name, msg_=caipu_info)

            for caipu_dict in caipu_req["result"]["list"]:
                cp_name = caipu_dict["cp_name"]
                zuofa = caipu_dict["zuofa"]
                texing = caipu_dict["texing"]
                tishi = caipu_dict["tishi"]
                tiaoliao = caipu_dict["tiaoliao"]
                yuanliao = caipu_dict["yuanliao"]

                self.caidan_moudl(cp_name=cp_name, zuofa=zuofa, texing=texing, tishi=tishi, tiaoliao=tiaoliao,
                                  yuanliao=yuanliao)
                print(caipu_dict)
        else:
            wx_send_msg(send_=self.t_name, msg_="菜谱🥘获取失败！")

    # 英汉名言
    def yinhanmingyan(self):
        yh = f"https://apis.tianapi.com/enmaxim/index?key={self.key}"
        yh_req = requests.get(yh, headers=glb_data.headers).json()
        print(yh_req)
        if yh_req["code"] == 200:
            en = yh_req["result"]["en"]
            zh = yh_req["result"]["zh"]

            print(en + "\n" + zh)
            wx_send_msg(send_=self.t_name, msg_=en + "\n" + zh)

        else:
            wx_send_msg(send_=self.t_name, msg_="格言📄获取失败！")

    # 添狗日记
    def tiangou(self):
        tiangou_url = f"https://apis.tianapi.com/tiangou/index?key={self.key}"
        tg_req = requests.get(tiangou_url, headers=glb_data.headers).json()
        print(tg_req)
        if tg_req["code"] == 200:
            tg_text = tg_req["result"]["content"]

            print(tg_text)
            wx_send_msg(send_=self.t_name, msg_=tg_text)
        else:
            wx_send_msg(send_=self.t_name, msg_="日记📄获取失败！")

    # 健康妙招
    def jiankang(self, jk_word):
        jk_url = f"https://apis.tianapi.com/healthskill/index?key={self.key}&word={jk_word}"
        jk_req = requests.get(jk_url, headers=glb_data.headers).json()
        print(jk_req)

        if jk_req["code"] == 200:
            a = 0
            jk_list = []
            for jk_push in jk_req["result"]["list"]:
                a += 1
                jk_list.append(f"""{jk_push["title"]}\n{a}:{jk_push["content"]}""")

            combined_str = "\n".join(jk_list)
            print(combined_str)
            wx_send_msg(send_=self.t_name, msg_=combined_str)

        else:
            wx_send_msg(send_=self.t_name, msg_="小贴士☺获取失败！")

    # ai机器人，可玩性还可以
    def robot(self, question):
        bot_url = "https://apis.tianapi.com/robot/index"
        data_ = {
            "key": self.key,
            "question": question,
            "mode": 0,
        }
        bot_req = requests.post(url=bot_url, data=data_).json()
        push_text = bot_req["result"]["reply"].replace("<br>", "\n")

        wx_send_msg(send_=self.t_name, msg_=push_text)
        print(push_text)

