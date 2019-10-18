from tkinter import *


class WabcoPage(Frame):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('300x300')
        self.create_page()

    def create_page(self):
        self.frame = Frame(self.root).pack()
        Label(self.frame, text="THis page is Wabco Label !").pack()
