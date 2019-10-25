import re
import os
import clr

import shutil
import zipfile
from datetime import datetime
from subprocess import Popen, PIPE, STDOUT
from tkinter.messagebox import *

# 此文件用于添加定义、变量
Desktop = os.path.join(os.path.expanduser('~'), "Desktop")
Av2_log = Desktop + "\\Av2_Output\\outfile.txt"
Av2_Input = Desktop + "\\Av2_Input"
Av2_Output = Desktop + "\\Av2_Output"
Analyze = Desktop + "\\Analyze"
base_path1 = "D:\\test\\Release\\log\\"  # Av2数据所在路径
pos = Desktop + "\\pos.txt"
Err_Position = Desktop + "\\Err.txt"  # 打印Av2Log中的Position的offset异常
stub_position = Av2_Output + "\\sub&position.txt"

stub_path = Desktop + "\\Av2_Output\\stub.txt"
meta_path = Desktop + "\\Av2_Output\\meta.txt"
seg_path = Desktop + "\\Av2_Output\\seg.txt"
pos_path = Desktop + "\\Av2_Output\\pos.txt"
prl1_path = Desktop + "\\Av2_Output\\prl1.txt"
prl2_path = Desktop + "\\Av2_Output\\prl2.txt"
prl9_path = Desktop + "\\Av2_Output\\prl9.txt"
prs1_path = Desktop + "\\Av2_Output\\prs1.txt"
prs4_path = Desktop + "\\Av2_Output\\prs4.txt"

list_ehp = []
list_ada = []
list_loc = []
Err = []
listtt = []

with open(Av2_log, 'r', encoding="utf-8") as f1:
    lists = f1.readlines()

with open(pos, 'r', encoding="utf-8") as file:
    tmp = file.readlines()

time = re.compile(r'\d+-\d+ \d+:\d+:\d+\.\d+')
pattern_ofs = re.compile(r'ofs=\d+,')
pattern_path = re.compile(r'path=\d+,')
pattern_speed = re.compile(r'speed=\d+,')

pat_Stub = re.compile(r'Stub: path=\d+')
pat_sub = re.compile(r'subPath=\d+')
pat_Pos = re.compile(r'Position: path=\d+')
pat_Pro_Long1 = re.compile(r'Profile Long: type=1')
pat_Pro_Long2 = re.compile(r'Profile Long: type=2')
pat_Pro_Long9 = re.compile(r'Profile Long: type=9')
pat_Pro_Sht1 = re.compile(r'Profile Short: type=1')
pat_Pro_Sht4 = re.compile(r'Profile Short: type=4')
pat_Meta = re.compile(r'Metadata')
pat_Seg = re.compile(r'Segment: ')
pat_time = re.compile(r'\d+-\d+ \d+:\d+:\d+\.\d+')
po = re.compile(r'path=\d+')
