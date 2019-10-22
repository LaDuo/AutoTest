from tkinter import *
from defi import *


class HQFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.map_names = None
        self.var = StringVar()
        self.createPage()

    def Av_position(self):  # 此函数为createPage函数中Button按钮的点击事件
        var = StringVar()
        with open(Av2_log, 'r', encoding='utf-8') as f:
            LogList = f.readlines()

    def AvLog(self):  # 将桌面上的Av2_Input文件夹中的Av2 Log合并放置在Av2_Output文件夹中的outfile.txt中
        files = os.listdir(Av2_Input)
        res = ""
        i = 1
        for file in files:
            if file.endswith(".txt"):
                i += 1
                title = "第%s章 %s" % (i, file[0:len(file) - 4])
                with open(Av2_Input + "\\" + file, "r", encoding='utf-8') as file:
                    content = file.read()
                    file.close()
                append = "\n%s\n\n%s" % (title, content)
                res += append
        with open(Desktop + "\\Av2_Output\\outfile.txt", "w", encoding='utf-8') as outFile:
            outFile.write(res)

    def CreateMoveMerge(self):
        # 创建根目录
        map_name = self.var.get()
        # 等待添加功能，在点击创建文件时，判断用户输入是否为空，若为空，则提示"输入为空，请输入回放路线！"

        # if
        try:
            if not os.path.exists(Analyze):
                os.mkdir(Analyze)
                print("创建成功")
        except FileExistsError:
            print("目录已存在")
        # 创建子文件夹
        print("正在创建子文件夹")
        str1 = os.path.join(Analyze, datetime.now().strftime("%Y-%m-%d-")) + map_name
        os.makedirs(str1)
        os.mkdir(os.path.join(str1, "Av2"))
        os.mkdir(os.path.join(str1, "EHPLOG"))
        os.mkdir(os.path.join(str1, "CONFIG"))
        # print("Create folders successful")
        print("正在复制Av2log到Analyze文件夹和Av2_Input文件夹中")
        # 将Av2Simulator中的Log复制一份至Analyze文件夹和Av2_Input文件夹中
        # Av2数据路径需要根据电脑配置更改
        base_path1 = "D:\\test\\Release\\log\\"  # Av2数据所在路径
        base_path2 = os.path.join(os.path.expanduser('~'), "Desktop") + "\\Av2_Input\\"
        base_path3 = os.path.join(os.path.expanduser('~'), "Desktop") + "\\Analyze\\" + \
                     datetime.now().strftime("%Y-%m-%d-") + map_name + "\\Av2"
        alllist = os.listdir(base_path1)
        for i in alllist:
            if "_Av2数据" in i:
                oldname = os.path.join(base_path1, i)
                newname1 = os.path.join(base_path2, i)
                newname2 = os.path.join(base_path3, i)
                shutil.copyfile(oldname, newname1)  # 拷贝到Av2_Input文件夹
                shutil.copyfile(oldname, newname2)  # 拷贝到Analyze文件夹
        # 将桌面上的Av2_Input文件夹中的Av2 Log合并放置在Av2_Output文件夹中的outfile.txt中
        print("正在合并生成outfile.txt")
        files = os.listdir(Av2_Input)
        res = ""
        i = 1
        for file in files:
            if file.endswith(".txt"):
                i += 1
                title = "第%s章 %s" % (i, file[0:len(file) - 4])
                with open(Av2_Input + "\\" + file, "r", encoding='utf-8') as file:
                    content = file.read()
                    file.close()
                append = "\n%s\n\n%s" % (title, content)
                res += append
        dirPath_out = Av2_Output
        if not os.path.exists(dirPath_out):
            os.mkdir(dirPath_out)
        with open(dirPath_out + "\\outfile.txt", "w", encoding='utf-8') as outFile:
            outFile.write(res)
        # ----------------------------------------------------------------
        # 删除Av2Simulator中的Log文件夹中的内容
        print("正在删除Avlog")
        for j in alllist:
            if ".txt" in j:
                path = os.path.join(base_path1, j)
                os.remove(path)

        # 压缩文件
        # print("正在压缩Avlog")
        # zip_name = base_path3 + '.zip'
        # z = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        # for dirpath, dirnames, filenames in os.walk(base_path3):
        #     fpath = dirpath.replace(base_path3, '')
        #     fpath = fpath and fpath + os.sep or ''
        #     for filename in filenames:
        #         z.write(os.path.join(dirpath, filename), fpath + filename)
        # z.close()

        # ---------------------------------
        print("正在下载EHPLOG")
        os.chdir(r'C:\\Users\\z1339\\Desktop')  # 自动下载EHPLOG至Analyze目录下的ALL文件夹中
        p = Popen("cmd.exe /c" + "C:\\Users\\z1339\\Desktop\\down.bat", stdout=PIPE, stderr=STDOUT)
        curline = p.stdout.readline()
        while curline != b'':
            print(curline)
            curline = p.stdout.readline()
        p.wait()
        print(p.returncode)
        print("正在转移EHPLOG")
        # ---------------------------------------------------------------
        # 将Analyze目录中的ALL文件夹中的所有文件拷贝至新建的回放路线文件夹中
        src = Analyze + "\\ALL"
        dst = str1 + "\\EHPLOG"
        ALL_list = os.listdir(src)
        for i in ALL_list:
            n1 = os.path.join(src, i)
            shutil.move(n1, dst)


    def DeleteAvLog(self):
        Avlog_path = "D:\\test\\Release\\log"
        Avlog1 = os.listdir(Avlog_path)
        for i in Avlog1:
            if ".txt" in i:
                path = os.path.join(Avlog_path, i)
                os.remove(path)
        Avlog2 = os.listdir(Av2_Input)
        for i in Avlog2:
            if ".txt" in i:
                path = os.path.join(Avlog_path, i)
                os.remove(path)
        Avlog3 = os.listdir(Av2_Output)
        for i in Avlog3:
            if ".txt" in i:
                path = os.path.join(Avlog_path, i)
                os.remove(path)

    def Ehp_position(self):
        pass

    def merge_info(self):  # 合并EHPLOG中adasisApp、ehrizonApp、localizationApp的INFO文件
        map_name = self.var.get()
        str1 = os.path.join(Analyze, datetime.now().strftime("%Y-%m-%d-")) + map_name
        folder = str1 + "\\EHPLOG"
        list_Info = os.listdir(folder)
        for i in list_Info:
            if i.startswith("eho") and "INFO" in i and "Nebu" in i:
                list_ehp.append(i)
            if i.startswith("ada") and "INFO" in i and "Nebu" in i:
                list_ada.append(i)
            if i.startswith("loc") and "INFO" in i and "Nebu" in i:
                list_loc.append(i)
        # adasis_INFO.txt
        ada_result = Desktop + "\\adasis_INFO.txt"
        file = open(ada_result, 'w')
        for a in list_ada:
            path = folder + "\\" + a
            for line in open(path):
                file.write(line)
            file.write("\n")
        file.close()
        # ehp_INFO.txt
        ada_result = Desktop + "\\ehp_INFO.txt"
        file = open(ada_result, 'w')
        for a in list_ehp:
            path = folder + "\\" + a
            for line in open(path):
                file.write(line)
            file.write("\n")
        file.close()
        # localization_INFO.txt
        ada_result = Desktop + "\\localization_INFO.txt"
        file = open(ada_result, 'w')
        for a in list_loc:
            path = folder + "\\" + a
            for line in open(path):
                file.write(line)
            file.write("\n")
        file.close()
        print("merger over")

        # 提取matchpt,gcj
        pattern = re.compile(r'matchpt,\d+\.\d+,\d+\.\d+')
        path_mapmatch = Desktop + "\\localization_INFO.txt"
        matchpt = Desktop + "\\matchpt.txt"
        gcj = Desktop + "\\gcj1.txt"
        with open(path_mapmatch, 'r', encoding="utf-8") as f:
            match = f.readlines()
        with open(matchpt, 'w', encoding='utf-8') as f:
            for i in range(len(match)):
                m = pattern.findall(match[i])
                if m:
                    n = str(m)
                    f.write(n[2:-2])
                    f.write('\n')
        pattern = re.compile(r'gcj1,\d+\.\d+,\d+\.\d+')
        path_mapmatch = Desktop + "\\localization_INFO.txt"
        with open(path_mapmatch, 'r', encoding="utf-8") as f:
            match = f.readlines()
        with open(gcj, 'w', encoding='utf-8') as f:
            for i in range(len(match)):
                m = pattern.findall(match[i])
                if m:
                    n = str(m)
                    f.write(n[2:-2])
                    f.write('\n')

    def download_EHPLOG(self):
        pass

    def createPage(self):  # 界面布局  下同
        # Label(self).grid(row=1, stick=W, pady=10)
        Label(self, text="This is HQ Page!").grid(row=0, column=1, columnspan=1)
        # ========================Av2 Log==========================
        # -----------------------------------------------------------------------
        Label(self, text="请输入回放的路线名：").grid(row=1, column=0)
        self.map_names = Entry(self, textvariable=self.var)
        self.map_names.grid(row=1, column=1)
        Button(self, text="创建文件夹", command=self.CreateMoveMerge).grid(row=1, column=2)
        # ----------------------------------------------------------------------------------------------
        Button(self, text="合并Av2Log", command=self.AvLog).grid(row=2, column=0)
        Button(self, text="删除所有的Av2Log", command=self.DeleteAvLog).grid(row=2, column=1)
        Button(self, text="获取Av2Log中的Position", command=self.Av_position).grid(row=2, column=2)

        # =======================Ehp Log===========================
        Button(self, text="获取EhpLog中的Position", command=self.Ehp_position).grid(row=3, column=0)
        Button(self, text="EHPLOG_INFO_Merge", command=self.merge_info).grid(row=3, column=1)


class WabcoFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):
        Label(self, text="This is Wabco Page!").pack()


class RockyFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):
        Label(self, text="This is Rocky Page!").pack()
