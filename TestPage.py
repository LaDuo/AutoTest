from tkinter import *
from AutoTestView import *


class TestPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('300x300')
        self.create_page()

    def create_page(self):
        self.HQPage = HQFrame(self.root)
        self.WabcoPage = WabcoFrame(self.root)
        self.RockyPage = RockyFrame(self.root)
        self.HQPage.pack()
        menubar = Menu(self.root)
        menubar.add_command(label="HQ", command=self.HQ)
        menubar.add_command(label="Wabco", command=self.Wabco)
        menubar.add_command(label="Rocky", command=self.Rocky)
        menubar.add_command(label="Quit", command=self.root.quit)
        self.root['menu'] = menubar  # 设置菜单栏

    def HQ(self):
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
