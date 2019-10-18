from tkinter import *


class HQFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):
        # Label(self).grid(row=1, stick=W, pady=10)
        Label(self, text="This is HQ Page!").pack()


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
