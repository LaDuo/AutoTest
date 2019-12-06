from tkinter import *
from defi import *


class HQFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.map_names = None
        self.var = StringVar()
        self.createPage()


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
        with open(Av2_log, "w", encoding='utf-8') as outFile:
            outFile.write(res)
        showinfo(title="合并Av Log到outfile文件！", message="合并成功！")

    def CreateMoveMerge(self):
        # 创建根目录
        map_name = self.var.get()
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
        base_path2 = Desktop + "\\Av2_Input\\"
        base_path3 = Desktop + "\\Analyze\\" + \
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
        # ---------------------------------------------------------------------
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
        # ---------------------------------------------------------------------
        print("正在下载EHPLOG")
        os.chdir(Desktop)  # 自动下载EHPLOG至Analyze目录下的ALL文件夹中
        p = Popen("cmd.exe /c" + Desktop + "\\downEhp.bat", stdout=PIPE, stderr=STDOUT)
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
        # ---------------------------------------------------------------
        print("正在下载conf")
        os.chdir(Desktop)  # 自动下载conf至Analyze目录下的ALL文件夹中
        p = Popen("cmd.exe /c" + Desktop + "\\downconf.bat", stdout=PIPE, stderr=STDOUT)
        curline = p.stdout.readline()
        while curline != b'':
            print(curline)
            curline = p.stdout.readline()
        p.wait()
        print(p.returncode)
        print("正在转移conf")
        # ---------------------------------------------------------------
        # 将Analyze目录中的ALL文件夹中的所有文件拷贝至新建的回放路线文件夹中
        src = Analyze + "\\ALL"
        dst = str1 + "\\CONFIG"
        ALL_list = os.listdir(src)
        for i in ALL_list:
            n1 = os.path.join(src, i)
            shutil.move(n1, dst)
        showinfo(title="Create Move Download Merge", message="Success！")

    def DeleteAvLog(self):
        # Avlog1 = os.listdir(base_path1)
        # for i in Avlog1:
        #     if ".txt" in i:
        #         path = os.path.join(base_path1, i)
        #         os.remove(path)
        Avlog2 = os.listdir(Av2_Input)
        for i in Avlog2:
            if ".txt" in i:
                path = os.path.join(Av2_Input, i)
                os.remove(path)
        Avlog3 = os.listdir(Av2_Output)
        for i in Avlog3:
            if ".txt" in i:
                path = os.path.join(Av2_Output, i)
                os.remove(path)
        showinfo(title="Delete AvLog", message="成功删除Av Log")

    def Sep_MSG(self):
        # stub msg
        t1 = threading.Thread(target=HQFrame.action, args=(self, stub_path, pat_Stub))
        t1.start()
        # position msg
        t2 = threading.Thread(target=HQFrame.action, args=(self, pos_path, pat_Pos))
        t2.start()
        # segment msg
        t3 = threading.Thread(target=HQFrame.action, args=(self, seg_path, pat_Seg))
        t3.start()
        # profile long type 1
        t4 = threading.Thread(target=HQFrame.action, args=(self, prl1_path, pat_Pro_Long1))
        t4.start()
        # profile long type 2
        t5 = threading.Thread(target=HQFrame.action, args=(self, prl2_path, pat_Pro_Long2))
        t5.start()
        # profile long type 9
        t6 = threading.Thread(target=HQFrame.action, args=(self, prl9_path, pat_Pro_Long9))
        t6.start()
        # profile short type 1
        t7 = threading.Thread(target=HQFrame.action, args=(self, prs1_path, pat_Pro_Sht1))
        t7.start()
        # profile short type 4
        t8 = threading.Thread(target=HQFrame.action, args=(self, prs4_path, pat_Pro_Sht4))
        t8.start()
        # Metadata
        t9 = threading.Thread(target=HQFrame.action, args=(self, meta_path, pat_Meta))
        t9.start()
        with open(pos_stub_path, 'w', encoding="utf-8") as file:
            for i in range(len(lists)):
                a = pat_stub.findall(lists[i])
                b = pat_Pos.findall(lists[i])
                if a:
                    file.write(str(lists[i]))
                elif b:
                    file.write(str(lists[i]))
        with open(slope_path, 'w', encoding="utf-8") as file:
            for i in range(len(lists)):
                a = av_slope_v.findall(lists[i])
                b = short.findall(lists[i])
                if a and b:
                    file.write(str(lists[i]))
        showinfo(title="提取MSG", message="成功提取各个MSG！")

    def action(self, route, pat,):
        pats = re.compile(pat)
        with open(route, 'w', encoding="utf-8") as file:
            for i in range(len(lists)):
                n = pats.findall(lists[i])
                if n:
                    file.write(lists[i])

    def draw_slope(self, path_id, value_list=[], ofs_list=[]):
        plt.clf()
        plt.plot(ofs_list, value_list)
        plt.title(path_id)
        plt.show()

    # 备份发送
    def ROBUSTNSS_(self):
        with open(slope_path, 'r', encoding="utf-8") as f:
            lir = f.readlines()
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
                self.draw_slope(path1, lir_value, lir_ofs)
                lir_value = []
                lir_ofs = []

    # 一次发送两个
    def BANDWIDTH_(self):
        with open(slope_path, 'r', encoding="utf-8") as f:
            lir = f.readlines()
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
                self.draw_slope(path1, lir_value, lir_ofs)
                lir_value = []
                lir_ofs = []

    def ShowSlope(self):
        ehp_result = Av2_Output + "\\prs4.txt"
        with open(ehp_result, 'r', encoding="utf-8") as f:
            tmp = f.readlines()
        slope_model = self.text.get(1.0, 2.0)
        if slope_model == "\n":
            showinfo(title="Error", message="未选择发送模式")
        if slope_model == "2\n":
            self.ROBUSTNSS_()
        elif slope_model == "3\n":
            self.BANDWIDTH_()

    def JudgePosition(self):
        flag = 0
        try:
            with open(pos_path, 'r', encoding="utf-8") as file:
                tmp = file.readlines()
            flag = 1
        except FileNotFoundError:
            showwarning(title="Warning", message=" <pos.txt>  File not found")
        if flag == 1:
            for i in range(len(tmp)):
                if i == len(tmp) - 1:
                    break
                j = i + 1
                ofs1 = str(pattern_ofs.findall(tmp[i]))
                ofs2 = str(pattern_ofs.findall(tmp[j]))
                path1 = str(pattern_path.findall(tmp[i]))
                path2 = str(pattern_path.findall(tmp[j]))
                ofs1 = int(re.sub(r'\D', "", ofs1))
                ofs2 = int(re.sub(r'\D', "", ofs2))
                path1 = int(re.sub(r'\D', "", path1))
                path2 = int(re.sub(r'\D', "", path2))
                # 相同path id情况下，offset递增，反之打印（忽略path id不同的情况）
                if path1 == 0:
                    continue
                if (path1 == path2) and (ofs2 >= ofs1):
                    continue
                elif (path1 == path2) and (ofs2 < ofs1):
                    Err.append(str(tmp[i]))
                    Err.append(str(tmp[j]))
                    Err.append('\n')
            with open(Err_Position, 'w', encoding="utf-8") as file:
                for i in range(len(Err)):
                    file.write(str(Err[i]))
                    file.write("\n")
            showinfo(title="判断", message="判断完成！")

    # 重构时是否发送stub
    def Send_Stub(self):
        with open(pos_stub_path, 'r', encoding='utf-8') as f:
            LogList = f.readlines()
        with open(Err_Stub_send, 'w', encoding="utf-8") as file:
            for i in range(len(LogList)):
                if i == len(LogList) - 2:
                    break
                j = i + 2
                k = i + 1
                # print("j = ", j, "k = ", k)
                pos1 = str(pat_Pos.findall(LogList[i]))
                pos2 = str(pat_Pos.findall(LogList[j]))
                stub = str(pat_stub.findall(LogList[k]))
                # print(type(pos1), type(offroad))
                if pos1 != "[]" and pos2 != "[]" and pos1 != offroad and pos1 != pos2:
                    if stub == "[]":
                        file.write(LogList[k])
                        file.write("\n")

        showinfo(title="Detect Stub MSG", message="检测完成")

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
        # ada_result = Av2_Output + "\\adasis_INFO.txt"
        # file = open(ada_result, 'w')
        # for a in list_ada:
        #     path = folder + "\\" + a
        #     for line in open(path):
        #         file.write(line)
        #     file.write("\n")
        # file.close()
        # ehp_INFO.txt
        ehp_result = Av2_Output + "\\ehp_INFO.txt"
        file = open(ehp_result, 'w')
        for a in list_ehp:
            path = folder + "\\" + a
            for line in open(path):
                file.write(line)
            file.write("\n")
        file.close()
        # localization_INFO.txt
        loc_result = Av2_Output + "\\localization_INFO.txt"
        file = open(loc_result, 'w')
        for a in list_loc:
            path = folder + "\\" + a
            for line in open(path):
                file.write(line)
            file.write("\n")
        file.close()
        showinfo("merger over")

        # 提取matchpt,gcj
        pattern = re.compile(r'matchpt,\d+\.\d+,\d+\.\d+')
        path_mapmatch = Av2_Output + "\\localization_INFO.txt"
        matchpt = Av2_Output + "\\matchpt.txt"
        gcj = Av2_Output + "\\gcj1.txt"
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
        path_mapmatch = Av2_Output + "\\localization_INFO.txt"
        with open(path_mapmatch, 'r', encoding="utf-8") as f:
            match = f.readlines()
        with open(gcj, 'w', encoding='utf-8') as f:
            for i in range(len(match)):
                m = pattern.findall(match[i])
                if m:
                    n = str(m)
                    f.write(n[2:-2])
                    f.write('\n')

    def BANDWIDTH(self):  # model为conf/ehorizon/ehorizon_conf.pb.txt中的profile_short_value_mode的配置
        self.text.delete(1.0, 2.0)
        model = 3  # model=3 表示BANDWIDTH模式，即 一次发送两个
        self.text.insert(END, model)

    def ROBUSTNSS(self):
        self.text.delete(1.0, 2.0)
        model = 2  # model=2 表示ROBUSTNSS模式，即 备份发送
        self.text.insert(END, model)

    # 删除两个月之前的log（Analyze）
    def clear(self):
        clr = os.listdir(Analyze)
        Date = time.strftime("%Y-%m-%d", time.localtime())
        year = Date[0:4]
        month = int(Date[5:7])
        for i in clr:
            # i_month = int(i[5:7])
            if i.startswith("ALL"):
                continue
            i_month = i[5:7]
            i_month = int(i_month)
            if i.startswith(year):
                if month - i_month >= 2:
                    shutil.rmtree(Analyze + "\\" + i)
            else:
                shutil.rmtree(Analyze + "\\" + i)

    def JudgeStub(self):
        flag = 0
        lir2 = []
        try:
            with open(stub_path, 'r', encoding="utf-8") as file:
                lir = file.readlines()
            flag = 1
        except FileNotFoundError:
            showerror(title="Warning!", message=" <stub.txt> File not found")
        if flag == 1:
            for i in range(len(lir)):
                if i == len(lir) - 1:
                    break
                j = i + 1
                id1 = stub_path_id.findall(lir[i])
                id2 = stub_path_id.findall(lir[j])
                ofs1 = str(stub_offset.findall(lir[i]))
                ofs2 = str(stub_offset.findall(lir[j]))
                ofs1 = int(re.sub(r'\D', "", ofs1))
                ofs2 = int(re.sub(r'\D', "", ofs2))
                last1 = stub_last.findall(lir[i])
                last2 = stub_last.findall(lir[j])
                if id1 == id2:
                    if ofs1 == ofs2:
                        if last1 == "true":
                            lir2.append("last1==true -->" + lir[i])
                            lir2.append("last1==true -->" + lir[j])
                    elif ofs1 < ofs2:
                        if last1 == "false":
                            lir2.append("last1==false-->" + lir[i])
                            lir2.append("last1==false-->" + lir[j])
                    else:
                        if ofs1 >= 7000:
                            continue
                        else:
                            lir2.append("ofs1 > ofs2 -->" + lir[i])
                            lir2.append("ofs1 > ofs2 -->" + lir[j])
            count = 0
            # 每组问题
            with open(Err_Stub_ofs, 'w', encoding="utf-8") as f:
                for n in range(len(lir2)):
                    f.write(lir2[n])
                    count += 1
                    if count == 2:
                        count = 0
                        f.write("======================\n")
            showinfo(title="完成", message="检测结束")

    def JudgeSegment(self):
        flag = 0
        lir2 = []
        cyc = []
        bri = []
        try:
            with open(seg_path, 'r', encoding="utf-8") as f:
                lir = f.readlines()
                flag = 1
        except FileNotFoundError:
            showerror(title="Warning!", message=" <seg.txt> File not found")
            flag = 0
        if flag == 1:
            for i in range(len(lir)):
                if i == len(lir) - 1:
                    break
                j = i + 1
                id1 = seg_path_id.findall(lir[i])
                id2 = seg_path_id.findall(lir[j])
                ofs1 = str(seg_offset.findall(lir[i]))
                ofs2 = str(seg_offset.findall(lir[j]))
                ofs1 = int(re.sub(r'\D', "", ofs1))
                ofs2 = int(re.sub(r'\D', "", ofs2))
                bridge = seg_bridge.findall(lir[i])
                cyclic1 = str(seg_cyclic.findall(lir[i]))
                cyclic1 = int(re.sub(r'\D', "", cyclic1))
                cyclic2 = str(seg_cyclic.findall(lir[j]))
                cyclic2 = int(re.sub(r'\D', "", cyclic2))
                if bridge:
                    bri.append(lir[i])
                if id1 == id2:
                    if ofs2 < ofs1:
                        lir2.append(lir[i])
                if cyclic1 == 0:
                    if cyclic2 != 1:
                        cyc.append(lir[j])

                if cyclic1 == 1:
                    if cyclic2 != 2:
                        cyc.append(lir[j])

                if cyclic1 == 2:
                    if cyclic2 != 3:
                        cyc.append(lir[j])

                if cyclic1 == 3:
                    if cyclic2 != 0:
                        cyc.append(lir[j])

            count = 0
            # 每组问题
            with open(Err_Segment, 'w', encoding="utf-8") as f:
                for n in range(len(lir2)):
                    f.write(lir2[n])
                    count += 1
                    if count == 2:
                        count = 0
                        f.write("======================\n")

    def GetCpu(self):
        flag = 0
        # try:
        #     client = InfluxDBClient(host="127.0.0.1", port=8086)
        #     flag = 1
        # except ConnectionRefusedError:
        #     showerror(title="ConnectionError", message="数据库连接失败！")
        #     flag = 0
        if flag == 0:
            # usr_cpu = client.query('select value from "processes_user" limit 1000', database="collectd")
            # ker_cpu = client.query('select * from "processes_syst" limit 1000', database="collectd")
            # phy_mem = client.query('select * from "processes_value" limit 1000', database="collectd")
            # sys_mem = client.query('select * from "memory_value" limit 1000', database="collectd")
            # free_cpu = client.query('select * from "cpu_value" limit 1000', database="collectd")

            showinfo(title="未完成", message="开发中")
            # with open(data_route+"\\cpu.txt", 'w', encoding="utf-8") as f:
            #     f.write("Result: {0}".format(usr_cpu))
            # with open(data_route+"\\memory.txt", 'w', encoding="utf-8") as f:
            #     f.write("Result: {0}".format(ker_cpu))

    def CpData(self):
        showinfo("HINT!", message="未开发")

    def createPage(self):  # 界面布局  下同
        # Label(self).grid(row=1, stick=W, pady=10)
        Label(self, text="This is HQ Page!").grid(row=0, column=1, columnspan=1)
        # ========================Av2 Log==========================
        # -----------------------------------------------------------------------
        Label(self, text="请输入回放的路线名：").grid(row=1, column=0)
        self.map_names = Entry(self, textvariable=self.var)
        self.map_names.grid(row=1, column=1)
        Button(self, width="20", height="1", text="START:创建文件夹", command=self.CreateMoveMerge).grid(row=1, column=2)
        # ----------------------------------------------------------------------------------------------
        Button(self, width="20", height="1", text="合并Av2Log", command=self.AvLog).grid(row=2, column=0)
        Button(self, width="20", height="1", text="END:删除所有的Av2Log", command=self.DeleteAvLog).grid(row=2, column=2)
        # 此按钮功能暂定
        # Button(self, text="获取Av2Log中的Position", command=self.Av_position).grid(row=2, column=2)
        # 判断Av Log中的position消息的offset
        self.text = Text(self, width="10", height="1")
        self.text.grid(row=5, column=0)
        Button(self, width="15", height="1", text="BANDWIDTH", command=self.BANDWIDTH).grid(row=5, column=1)
        Button(self, width="15", height="1", text="ROBUSTNSS", command=self.ROBUSTNSS).grid(row=5, column=2)
        Button(self, width="20", height="1", text="显示Slope", command=self.ShowSlope).grid(row=5, column=3)
        Button(self, width="20", height="1", text="判断Position的offset", command=self.JudgePosition).grid(row=4, column=0)
        Button(self, width="20", height="1", text="提取各个MSG", command=self.Sep_MSG).grid(row=3, column=0)
        # =======================Ehp Log===========================
        Button(self, width="20", height="1", text="判断Stub是否发送", command=self.Send_Stub).grid(row=3, column=1)
        Button(self, width="20", height="1", text="EHPLOG_INFO_Merge", command=self.merge_info).grid(row=4, column=1)
        Button(self, width="20", height="1", text="复制matchpt和gcj", command=self.CpData).grid(row=2, column=1)
        Button(self, width="20", height="1", text="清空上上个月的log", command=self.clear).grid(row=6, column=0)
        Button(self, width="20", height="1", text="stub_offset是否递增", command=self.JudgeStub).grid(row=6, column=1)
        Button(self, width="20", height="1", text="segment消息检测", command=self.JudgeSegment).grid(row=6, column=2)
        Button(self, width="20", height="1", text="提取性能数据", command=self.GetCpu).grid(row=7, column=0)


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
