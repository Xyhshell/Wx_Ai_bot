from pkg.log import print_

# 全局变量
from pkg import glb_data


def user_list_():
    """
    查看用户列表
    :return:
    """
    with open(file=glb_data.config_path, mode="r", encoding="utf-8") as de_f:
        data = de_f.read()
        user_list = data.split(",")
        print_("用户列表：", user_list)
        str_user = ""
        list_len = len(user_list)
        for i in range(0, list_len):
            text = f"""✅{user_list[i]}\n"""
            str_user += text
        print(str_user)
        return str_user


def cat(cat_user):
    """
    # 查看用户
    :param cat_user:
    :return:
    """
    with open(file=glb_data.config_path, mode="r", encoding="utf-8") as f:
        data = f.read()
        user_list = data.split(",")
        if cat_user in user_list:
            # print("白名单用户：", cat_user)
            return True
        else:
            # print("不是白名单用户！")
            return False


def add_user(ad_user):
    """
    添加用户，使用内建指令添加wechat:id(昵称)
    :return:
    """
    with open(file=glb_data.config_path, mode="r", encoding="utf-8") as f:
        data = f.read()
        user_list = data.split(",")
        if ad_user not in user_list:
            with open(file=glb_data.config_path, mode="a", encoding="utf-8") as ad_f:
                ad_f.write(f",{ad_user}")
                print(f"添加用户：{ad_user}成功！")
                print_(f"添加用户：{ad_user}成功！")
                # str_user = ",".join(user_list)
                # print(str_user)
                return f"添加用户：{ad_user}成功！"
        else:
            print(f"{ad_user}已是白名单用户！")
            print_(f"{ad_user}已是白名单用户！")
            return f"{ad_user}已是白名单用户！"


def del_user(de_user):
    """
    删除用户，使用内建指令删除wechat:id(昵称)
    :return:
    """
    with open(file=glb_data.config_path, mode="r", encoding="utf-8") as de_f:
        data = de_f.read()
        user_list = data.split(",")
        if de_user in user_list:
            user_list.remove(de_user)
            str_user = ",".join(user_list)
            with open(file=glb_data.config_path, mode="w", encoding="utf-8") as r_f:
                r_f.write(str_user)
            print(f"删除用户：{de_user}成功！")
            print_(f"删除用户：{de_user}成功！")
            print(str_user)
            return f"删除用户：{de_user}成功！"

        else:
            print("不存在此用户！")
            print_(f"{de_user}不存在此用户！")
            return f"{de_user}不存在此用户！"
