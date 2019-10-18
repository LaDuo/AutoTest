from tkinter import *


class RockyPage(Frame):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('300x300')
        self.create_page()

    def create_page(self):
        self.frame = Frame(self.root).pack()
        Label(self.frame, text="THis page is Rocky Label !").pack()
