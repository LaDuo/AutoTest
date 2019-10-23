import re
import os
from tkinter import *


# 此文件用于添加定义、变量
Desktop = os.path.join(os.path.expanduser('~'), "Desktop")
Av2_log = Desktop + "\\Av2_Output\\outfile.txt"
Av2_Input = Desktop + "\\Av2_Input"
Av2_Output = Desktop + "\\Av2_Output"
Analyze = Desktop + "\\Analyze"
base_path1 = "D:\\test\\Release\\log\\"  # Av2数据所在路径

list_ehp = []
list_ada = []
list_loc = []


Desktop = os.path.join(os.path.expanduser('~'), "Desktop")
pos = Desktop + "\\pos.txt"
Err_Position = Desktop + "\\Err.txt"

with open(pos, 'r', encoding="utf-8") as file:
    tmp = file.readlines()

position = re.compile(r'\d+-\d+ \d+:\d+:\d+\.\d+')
pattern_ofs = re.compile(r'ofs=\d+,')
pattern_path = re.compile(r'path=\d+,')
pattern_speed = re.compile(r'speed=\d+,')
Err = []


def JudgePosition():
    flag = True
    for i in range(len(tmp)):
        if i == len(tmp) - 1:
            break
        j = i + 1
        time = position.findall(tmp[i])
        speed1 = str(pattern_speed.findall(tmp[i]))
        speed2 = str(pattern_speed.findall(tmp[j]))
        ofs1 = str(pattern_ofs.findall(tmp[i]))
        ofs2 = str(pattern_ofs.findall(tmp[j]))
        path1 = str(pattern_path.findall(tmp[i]))
        path2 = str(pattern_path.findall(tmp[j]))
        speed1 = re.sub(r'\D', "", speed1)
        speed2 = re.sub(r'\D', "", speed2)
        ofs1 = re.sub(r'\D', "", ofs1)
        ofs2 = re.sub(r'\D', "", ofs2)
        path1 = re.sub(r'\D', "", path1)
        path2 = re.sub(r'\D', "", path2)
        if path1 == 0:
            continue
        if ofs2 > ofs1 and path1 == path2:
            print("HAHAHAHAHAHAHAHHA", ofs2, ofs1)
            flag = True
        elif ofs2 == ofs1 and speed1 == 0 and speed2 == 0:
            flag = True
        elif ofs2 < ofs1 and path1 != path2:
            flag = True
        elif ofs2 < ofs1 and path1 == path2:
            Err.append(str(tmp[i]))
            Err.append(str(tmp[j]))
            print(time)
            print(ofs2, ofs1, speed2, speed1, path2, path1)



if __name__ == '__main__':
    JudgePosition()
    with open(Err_Position, 'w', encoding="utf-8") as file:
        for i in range(len(Err)):
            file.write(str(Err[i]))
            file.write("\n")
