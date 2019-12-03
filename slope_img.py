import re
import os
import numpy as np
import matplotlib.pyplot as plt
print("""
# #####################################################使用须知#########################################################
#                                                 文件必须放置在桌面上
#                          其次是在运行前，手动从ehorizonApp.INFO文件中提取出profile short slope 
#                                             这个程序只能用来显示slope,分场景测试
# #####################################################################################################################
""")
pattern1 = re.compile(r'Profile Short: type=4')
pattern2 = re.compile(r',sl:\d+')
pattern3 = re.compile(r'value\d*=\d*')
pattern4 = re.compile(r'v0: \d{3}')
pattern5 = re.compile(r'v1: \d{3}')
llist = []

basic_path = os.path.join(os.path.expanduser("~"), "Desktop")


def full_list(path1):
    with open(path1, 'r', encoding="utf-8") as f:
        lists = f.readlines()
    return lists


def ret_lis1(lis):
    for i in range(len(lis)):
        if i == len(lis) - 1:
            break
        n1 = pattern4.findall(lis[i])
        str1 = str(n1)
        str1 = re.sub(r'\D', "", str1)
        if str1 != '1023':
            llist.append(int(str1))
    return llist


def ret_lis2(lis):
    for i in range(len(lis)):
        if i == len(lis) - 1:
            break
        n1 = pattern4.findall(lis[i])
        n2 = pattern5.findall(lis[i])
        str1 = str(n1)
        str2 = str(n2)
        str1 = str1[6:9]
        str2 = str2[6:9]
        llist.append(int(str1))
        if str2 != "102":
            llist.append(int(str2))
    return llist


def ret_lis3(lis):
    for i in range(len(lis)):
        if i == len(lis) - 1:
            break
        n1 = pattern2.findall(lis[i])
        str1 = str(n1)
        str1 = re.sub(r'\D', "", str1)
        if str1 != '1023':
            llist.append(int(str1))
    return llist


def prints(flag):
    folder = input("输入数据的文件名:")
    path1 = basic_path + "\\" + folder
    lis = full_list(path1)
    if flag == 1:
        li = ret_lis1(lis)
    elif flag == 2:
        li = ret_lis2(lis)
    elif flag == 3:
        li = ret_lis3(lis)
    length = len(li)
    lens = length // 500
    end = length - lens * 500
    on_off = input("1.多图显示    2.单图显示\n")
    if on_off == '1':
        for i in range(lens):
            t1 = i * 500
            t2 = (i + 1) * 500
            sl = li[t1: t2]
            x = range(0, 500)
            plt.plot(x, sl, label="First line", linewidth=1, color='r', marker='o', markerfacecolor='blue',
                     markersize=1)
            plt.xlabel("Unit")
            plt.ylabel("Slope")
            plt.title("Slope/Unit\n"
                      "Check it out")
            plt.legend()
            plt.show()
        sl = li[t2: length]
        x = range(0, end)
        plt.plot(x, sl, label="First line", linewidth=2, color='r', marker='o', markerfacecolor='blue', markersize=1)
        plt.xlabel("Unit")
        plt.ylabel("Slope")
        plt.title("Slope/Unit\n"
                  "Check it out")
        plt.legend()
        plt.show()
    elif on_off == '2':
        sl = li[0: length]
        x = range(0, length)
        y1 = np.arange(450, 550)
        y1 = list(y1)
        y = range(len(y1))
        plt.yticks(range(len(y)), y)
        plt.plot(x, sl, label="First line", linewidth=2, color='r', marker='o', markerfacecolor='blue', markersize=1)
        plt.xlabel("Unit")
        plt.ylabel("Slope")
        plt.title("Slope/Unit\n"
                  "Check it out")
        plt.legend()
        plt.show()
    else:
        print("Wrong number,try it again")


if __name__ == '__main__':
    flag = 0
    str_in = input("请输入模式（1 表示单：v0    2表示双：v0、v1     3表示：sl）： ")
    if str_in == "1":
        flag = 1
        prints(flag)
    elif str_in == "2":
        flag = 2
        prints(flag)
    elif str_in == "3":
        flag = 3
        prints(flag)
    else:
        print("Wrong Number!!")
