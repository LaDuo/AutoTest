import re
import os

# from defi import *

Desktop = os.path.join(os.path.expanduser('~'), "Desktop")
pos = Desktop + "\\pos.txt"

with open(pos, 'r', encoding="utf-8") as file:
    tmp = file.readlines()

pattern_position = re.compile(r'Position: path=\d+, ofs=\d+, speed=\d+')


def JudgePosition():
    for i in range(len(tmp)):
        if i == len(tmp) - 1:
            break
        j = i + 1
        fir = pattern_position.findall(tmp[i])
        las = pattern_position.findall(tmp[j])
        str_fir = str(fir)
        str_las = str(las)
        print(str_fir)
        speed1 = str_fir[35:37]
        speed2 = str_las[35:37]
        ofs1 = str_fir[25:27]
        ofs2 = str_las[25:27]
        path1 = str_fir[17:19]
        path2 = str_las[17:19]


if __name__ == '__main__':
    JudgePosition()

