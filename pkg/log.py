import os
import datetime

# 全局变量
from pkg import glb_data

print(os.getcwd())
file_dir = os.path.join(os.getcwd(), glb_data.log_path)
print(file_dir)
if not os.path.exists(file_dir):
    os.makedirs(file_dir)

log_name = 'log.txt'  # 日志文件名称
filename = os.path.join(file_dir, log_name)
print(filename)

rewrite_print = print


def print_(*arg):
    now_time = datetime.datetime.now()
    str_ti = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')

    # 重写打印
    # rewrite_print(*arg)
    # rewrite_print(str_ti, file=open(filename, mode="a", encoding="utf-8"))  # 写入文件
    rewrite_print(str_ti, "*\n", *arg, file=open(filename, mode="a", encoding="utf-8"))  # 写入文件


if __name__ == '__main__':
    print_(f'日志存放地址1: {filename}')
