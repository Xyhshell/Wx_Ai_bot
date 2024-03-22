# 内部推送
from pkg.wx_msg_all import *
from pkg.log import print_
from pkg.user import cat

# 插件
from pkg import ip
from pkg import cityWeather
from pkg import H_app
from pkg import sfly
from pkg import txai
from pkg import user
from pkg import gpt35

# 全局变量
from pkg import glb_data

# 管理员菜单
admin_text = """🐲年行大运: 尊敬的管理员👍
@ip : QG的docker-ip😘
@用户 ： 查看用户列表
@添加 ： 添加✅白名单用户
@删除 ： 删除❎白名单用户
------------------
- @si : 思知Robots + 
- @qy : 青云Robots +
- @jk ： 💪 +
- @ai ： 👩‍💻 +"""

# 普通用户菜单
help_text = """🐲《句应》: 支持关键字👍
@help : 显示关键字菜单👨‍🎓
@忘情水 : 🔥一句
@句子 : 英📋汉句
@笑话 : 添🐶日记
- @菜谱 ：做🍳方式 +
- @天气 ：查🌅状态 +
- @s : 讯飞文本🎊AI默认
- @t : 混元文本🚀模型
- @ps : 讯飞图片🌆(bate)
- @pt : 混元图片🌇(bate）
- @ca : ChatGpt(限额)"""


class AdminMian(object):
    def __init__(self, name_, msg_content):
        # 管理员享有的关键字
        self.admin_key = ["@admin", "@ip", "@用户", "@添加", "@删除", "@si", "@qy", "@jk", "@ai"]

        # 继承对象载荷
        self.name = name_
        self.msg = msg_content
        print(f"{self.name}: {self.msg}")

        # 用户白名单
        self.user_root = cat(cat_user=name_)
        # 启动天聚对象
        self.tianju = H_app.TianJu(t_name=self.name)

    def main_key(self):
        if self.msg == '@admin':
            wx_send_msg(send_=self.name, msg_=admin_text)
        elif self.msg == '@ip':
            push_text = ip.getip()
            wx_send_msg(send_=self.name, msg_=push_text)
        elif self.msg == '@用户':
            user_ = user.user_list_()
            wx_send_msg(send_=self.name, msg_=user_)
        # 内建用户添加
        elif '@添加' in self.msg:
            a_user = self.msg.replace("@添加 ", "")
            re_p = user.add_user(ad_user=a_user)
            wx_send_msg(send_=self.name, msg_=re_p)

        # 内建用户删除
        elif '@删除' in self.msg:
            d_user = self.msg.replace("@删除 ", "")
            re_d = user.del_user(de_user=d_user)
            wx_send_msg(send_=self.name, msg_=re_d)

        # todo:后续四个慢回复bot
        elif "@si" in self.msg:
            c = self.msg.replace("@si ", "")
            H_app.sizhi(t_name=self.name, sizi_word=c)
        elif "@qy" in self.msg:
            d = self.msg.replace("@qy ", "")
            H_app.qingyunke(t_name=self.name, qy_word=d)
        elif "@jk" in self.msg:
            f = self.msg.replace("@jk ", "")
            self.tianju.jiankang(jk_word=f)
        elif "@ai" in self.msg:
            g = self.msg.replace("@ai ", "")
            self.tianju.robot(question=g)

    def open_user(self):
        if self.msg == '@help':
            wx_send_msg(send_=self.name, msg_=help_text)
        elif self.msg == '@忘情水':
            H_app.one(t_name=self.name)
        elif self.msg == "@句子":
            self.tianju.yinhanmingyan()
        elif self.msg == "@笑话":
            self.tianju.tiangou()
        elif "@菜谱" in self.msg:
            e = self.msg.replace("@菜谱", "")
            self.tianju.caipu(key_word=e)
        elif "@天气" in self.msg:
            b = self.msg.replace("@天气", "")
            wx_send_msg(send_=self.name, msg_=f"开始查询：{b}")
            cityWeather.moji_weather(name_t=self.name, city_=b)

        elif "@s" in self.msg:
            s = self.msg.replace("@s", "")
            sfly.sf_word(s_name=self.name, ides_=s)
        elif "@ps" in self.msg:
            sp = self.msg.replace("@ps", "")
            sfly.sf_pic(s_name=self.name, ides_=sp)

        elif "@t" in self.msg:
            t = self.msg.replace("@t", "")
            txai.tx_msg(t_name=self.name, tx_word=t)
        elif "@pt" in self.msg:
            tp = self.msg.replace("@pt", "")
            txai.tx_pic(t_name=self.name, tx_pic_=tp)

        elif "@ca" in self.msg:
            ca = self.msg.replace("@ca", "")
            gpt35.ask(user_=self.name, q_msg=ca)

        else:
            # 暂时接替空任务对话
            print(f"\n\n{self.msg}\n👌\n")
            print_(f"👌讯飞处理{self.name}：{self.msg}")
            # 进入讯飞Ai
            sfly.sf_word(s_name=self.name, ides_=self.msg)

    def user_main(self):
        """
        用户甄别函数，区分管理员与普通用户，进行命令分配
        :return:
        """
        # try:
        #     key = self.msg.split(" ")[0]
        # except Exception as e:
        #     print(e)
        #     key = self.msg.split("")[0]

        try:
            key = self.msg.split(" ")[0]

            if key in self.admin_key:
                if self.name == glb_data.root:
                    wx_send_msg(send_=self.name, msg_=f"尊敬的管理员🍹:\n开始为您处理:{self.msg}")
                    self.main_key()
                else:
                    wx_send_msg(send_=self.name, msg_=f"￥ 非法用户，无权使用管理员指令😝")
                    exit()

            elif self.name == glb_data.root:
                wx_send_msg(send_=self.name, msg_=f"尊敬的创世者🌻:\n开始为您处理:{self.msg}")
                self.open_user()
            elif self.user_root:
                wx_send_msg(send_=self.name, msg_=f"欢迎使用《句应》👏\n用户{self.name} 开始为您处理:\n{self.msg}")
                self.open_user()

        except Exception as e:
            print(e)
            wx_send_msg(send_=glb_data.root, msg_=f"😡用户：{self.name}\n" + f"请求消息{self.msg}\n" + f"报错信息：\n{e}")


# --------------------------------------------------------
# docker - chat 检测
def info_():
    while True:
        try:
            r1 = requests.get(glb_data.mychat_url).text
            if r1 == "healthy":
                break
            else:
                sleep(3)
        except Exception as e:
            push_wx_main(uh=e)
            sleep(3)
    try:
        # 仅发送管理员
        wx_send_msg(send_=glb_data.root, msg_=admin_text)
    except Exception as e:
        push_wx_main(uh=e)
        info_()
