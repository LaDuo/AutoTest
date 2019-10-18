from tkinter import *
from HQ import *
from Wabco import *
from Rocky import *


class TestPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('300x300')
        self.create_page()

    def HQ(self):
        self.frame.destroy()
        HQPage(self.root)

    def Wabco(self):
        self.frame.destroy()
        WabcoPage(self.root)

    def Rocky(self):
        self.frame.destroy()
        RockyPage(self.root)

    def create_page(self):
        self.frame = Frame(self.root)
        self.frame.pack()
        Label(self.frame, text="Choose your project !").pack()

        menubar = Menu(self.root)
        menubar.add_command(label="HQ", command=self.HQ)
        menubar.add_command(label="Wabco", command=self.Wabco)
        menubar.add_command(label="Rocky", command=self.Rocky)
        menubar.add_command(label="Quit", command=self.frame.quit)

        self.root.config(menu=menubar)

