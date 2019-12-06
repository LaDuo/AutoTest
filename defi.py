import re
import os
import threading
import time
import requests
import clr
import PySimpleGUI as sg
from influxdb import InfluxDBClient
import shutil
import zipfile
import matplotlib.pyplot as plt
from datetime import datetime
from subprocess import Popen, PIPE, STDOUT
from tkinter.messagebox import *

# 此文件用于添加定义、变量
Desktop = os.path.join(os.path.expanduser('~'), "Desktop")
Av2_log = Desktop + "\\Av2_Output\\outfile.txt"
Av2_Input = Desktop + "\\Av2_Input"
Av2_Output = Desktop + "\\Av2_Output"
Analyze = Desktop + "\\Analyze"
# --------------------------------------------------------
base_path1 = "D:\\test\\Release\\log\\"  # Av2数据所在路径     重点关注   Av2数据路径需要根据电脑配置更改
# --------------------------------------------------------
global model

with open(Av2_log, 'r', encoding="utf-8") as file:
    lists = file.readlines()

Err_Position = os.path.join(Av2_Output, "Err_Pos.txt")  # 打印Av2Log中的Position的offset异常
Err_Stub_ofs = os.path.join(Av2_Output, "Err_Stub_ofs.txt")
Err_Stub_send = os.path.join(Av2_Output, "Err_Stub_send.txt")
Err_Segment = os.path.join(Av2_Output, "Err_Segment.txt")
stub_position = os.path.join(Av2_Output, "sub&position.txt")
stub_path = os.path.join(Av2_Output, "stub.txt")
meta_path = os.path.join(Av2_Output, "meta.txt")
seg_path = os.path.join(Av2_Output, "seg.txt")
pos_path = os.path.join(Av2_Output, "pos.txt")
prl1_path = os.path.join(Av2_Output, "prl1.txt")
prl2_path = os.path.join(Av2_Output, "prl2.txt")
prl7_path = os.path.join(Av2_Output, "prl7.txt")
prl9_path = os.path.join(Av2_Output, "prl9.txt")
prs1_path = os.path.join(Av2_Output, "prs1.txt")
prs4_path = os.path.join(Av2_Output, "prs4.txt")
pos_stub_path = os.path.join(Av2_Output, "pos_stub.txt")
slope_path = os.path.join(Av2_Output, "slope.txt")
gcj_Inspector = "D:\\test\\old_dateBase\\DatabaseInspector\\gcj.csv"
match_Inspector = "D:\\test\\old_dateBase\\DatabaseInspector\\match.csv"

list_ehp = []
list_ada = []
list_loc = []
Err = []
listtt = []

list_items = [1, 2, 3, 4]

pattern_time = re.compile(r'\d+-\d+ \d+:\d+:\d+\.\d+')
pattern_ofs = re.compile(r'ofs=\d+,')
pattern_path = re.compile(r'path=\d+,')
pattern_speed = re.compile(r'speed=\d+,')
pat_stub = re.compile(r'Stub: path=0,')
pat_Stub = re.compile(r'Stub: path=\d+')
pat_sub = re.compile(r'subPath=\d+')
pat_Pos = re.compile(r'Position: path=\d+')
pat_Pro_Long1 = re.compile(r'Profile Long: type=1')
pat_Pro_Long2 = re.compile(r'Profile Long: type=2')
pat_Pro_Long7 = re.compile(r'Profile Long: type=7')
pat_Pro_Long9 = re.compile(r'Profile Long: type=9')
pat_Pro_Sht1 = re.compile(r'Profile Short: type=1')
pat_Pro_Sht4 = re.compile(r'Profile Short: type=4')
pat_Meta = re.compile(r'Metadata')
pat_Seg = re.compile(r'Segment: ')
pat_time = re.compile(r'\d+-\d+ \d+:\d+:\d+\.\d+')
po = re.compile(r'path=\d+')
short = re.compile(r'Profile Short: type=4')
av_slope_v = re.compile(r'value=\d+')
av_slope_v1 = re.compile(r'value1=\d+')
eh_slope_v = re.compile(r'v0:\s\d{3}')
eh_slope_v1 = re.compile(r'v1:\s\d{3}')

# stub message RE
stub_path_id = re.compile(r'path=\d+')
stub_offset = re.compile(r'ofs=\d+')
stub_last = re.compile(r'isLastStubAtOffset=\w+')
offroad = "['Position: path=2']"

# segment message RE
seg_path_id = re.compile(r'path=\d+')
seg_offset = re.compile(r'ofs=\d+')
seg_bridge = re.compile(r'isBridge=av2_true')
seg_cyclic = re.compile(r'cyclic=\d')

# InfluxDB
data_route = "D:\\test\\InfluxDBdata"

# profile short slope
slope_path_id = re.compile(r'path=\d+')
slope_value = re.compile(r'value=\d+')
slope_value1 = re.compile(r'value1=\d+')
slope_cyc = re.compile(r'cyclic=\d')
slope_ofs = re.compile(r'offs=\d+')
slope_dis = re.compile(r'distance1=\d+')
