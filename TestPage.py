from tkinter import *
from AutoTestView import *


class TestPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('600x300')
        self.create_page()

    def create_page(self):
        self.HQPage = HQFrame(self.root)  # 用Frame容器的派生类，来创建HQ的功能验证界面  下同
        self.WabcoPage = WabcoFrame(self.root)  # 创建Wabco的功能验证界面
        self.RockyPage = RockyFrame(self.root)  # 创建Rocky的功能验证界面
        self.HQPage.pack()  # 第一个显示HQ
        menubar = Menu(self.root)  # 制作菜单栏
        menubar.add_command(label="HQ", command=self.HQ)  # 将HQ作为菜单栏中的一项  下同
        menubar.add_command(label="Wabco", command=self.Wabco)
        menubar.add_command(label="Rocky", command=self.Rocky)
        menubar.add_command(label="Quit", command=self.root.quit)
        self.root['menu'] = menubar  # 设置菜单栏

    def HQ(self):  # 在点击HQ菜单时，显示HQ界面，并将其他菜单界面隐藏  下同
        self.HQPage.pack()
        self.WabcoPage.pack_forget()
        self.RockyPage.pack_forget()

    def Wabco(self):
        self.WabcoPage.pack()
        self.HQPage.pack_forget()
        self.RockyPage.pack_forget()

    def Rocky(self):
        self.RockyPage.pack()
        self.HQPage.pack_forget()
        self.WabcoPage.pack_forget()
