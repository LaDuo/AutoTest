import re
import os
import shutil
import zipfile
from datetime import datetime
from subprocess import Popen, PIPE, STDOUT
import os

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
