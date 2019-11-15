from TestPage import *

main_window = Tk()  # 创建一个窗口对象
main_window.title(" Auto Test !")  # 窗口的标题
TestPage(main_window)  # 将该对象传入TestPage类中
main_window.mainloop()  # 消息循环
