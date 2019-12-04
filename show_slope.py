import re
import os
import matplotlib.pyplot as plt

Desktop = os.path.join(os.path.expanduser("~"), "Desktop")
route = Desktop + "\\Av2_Output\\slope.txt"

slope_path_id = re.compile(r'path=\d+')
slope_value = re.compile(r'value=\d+')
slope_value1 = re.compile(r'value1=\d+')
slope_cyc = re.compile(r'cyclic=\d')
slope_ofs = re.compile(r'offs=\d+')

with open(route, 'r', encoding="utf-8") as f:
    lir = f.readlines()


def draw(path_id, value_list=[], ofs_list=[]):
    plt.clf()
    plt.plot(ofs_list, value_list)
    plt.title(path_id)
    plt.show()


# 一次发送两个slope
def BANDWIDTH():
    lir_value = []
    lir_ofs = []
    for i in range(len(lir)):
        if i == len(lir) - 1:
            break
        j = i + 1
        value = str(slope_value.findall(lir[i]))
        value1 = str(slope_value1.findall(lir[i]))
        value = int(re.sub(r'\D', "", value))
        value1 = int(re.sub(r'\D', "", value1)[1:])
        offset = str(slope_ofs.findall(lir[i]))
        offset = int(re.sub(r'\D', "", offset))
        path1 = str(slope_path_id.findall(lir[i]))
        path2 = str(slope_path_id.findall(lir[j]))
        path1 = int(re.sub(r'\D', "", path1))
        path2 = int(re.sub(r'\D', "", path2))
        lir_value.append(value)
        lir_value.append(value1)
        lir_ofs.append(offset)
        if path1 != path2:
            draw(path1, lir_value, lir_ofs)
            lir_value = []
            lir_ofs = []


def ROBUSNESS():
    lir_value = []
    lir_ofs = []
    for i in range(len(lir)):
        if i == len(lir) - 1:
            break
        j = i + 1
        value = str(slope_value.findall(lir[i]))
        value = int(re.sub(r'\D', "", value))
        offset = str(slope_ofs.findall(lir[i]))
        offset = int(re.sub(r'\D', "", offset))
        path1 = str(slope_path_id.findall(lir[i]))
        path2 = str(slope_path_id.findall(lir[j]))
        path1 = int(re.sub(r'\D', "", path1))
        path2 = int(re.sub(r'\D', "", path2))
        if value:
            lir_value.append(value)
            lir_ofs.append(offset)
        if path1 != path2:
            draw(path1, lir_value, lir_ofs)
            lir_value = []
            lir_ofs = []


if __name__ == '__main__':
    ROBUSNESS()
