from tkinter import *
from defi import *


class HQFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def position(self):  # 此函数为createPage函数中Button按钮的点击事件
        var = StringVar()
        with open(Av2_log, 'r', encoding='utf-8') as f:
            LogList = f.readlines()
        # var.set(LogList[0])
        # Label(self, bg='red', width=5, textvariable=var).pack()
        self.T = Text(self, width=300, height=3)
        self.T.pack()
        self.T.insert('1.0', chars=LogList[0])

    def createPage(self):  # 界面布局  下同
        # Label(self).grid(row=1, stick=W, pady=10)
        Label(self, text="This is HQ Page!").pack()
        Button(self, text="GetPosition", command=self.position).pack()


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
