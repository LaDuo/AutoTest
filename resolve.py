from tkinter import *
# base = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F]
base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]


# bin2dec
# 二进制 to 十进制: int(str,n=10)
def bin2dec(string_num):
    return str(int(string_num, 2))


# hex2dec
# 十六进制 to 十进制
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))


# dec2bin
# 十进制 to 二进制: bin()
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


# dec2hex
# 十进制 to 八进制: oct()
# 十进制 to 十六进制: hex()
def dec2hex(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 16)
        mid.append(base[rem])

    return ''.join([str(x) for x in mid[::-1]])


# hex2tobin
# 十六进制 to 二进制: bin(int(str,16))
def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))


# bin2hex
# 二进制 to 十六进制: hex(int(str,2))
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))


def add(a):
    s = ''
    e = '0'
    if len(a) < 8:
        d = 8 - len(a)
        for i in range(d):
            s += e
    s += a
    return s


def calc():
    global E1, t2, t3
    global string
    string = E1.get()
    s1 = string[0:2]
    s2 = string[3:5]
    s3 = string[6:8]
    s4 = string[9:11]
    s5 = string[12:14]
    s6 = string[15:17]
    s7 = string[18:20]
    s8 = string[21:23]
    a1 = hex2bin(s1)
    # print(add(a1))
    a2 = hex2bin(s2)
    b2 = add(a2)
    # print(add(a2))
    a3 = hex2bin(s3)
    b3 = add(a3)
    # print(add(a3))
    a4 = hex2bin(s4)
    b4 = add(a4)
    # print(add(a4))
    a5 = hex2bin(s5)
    b5 = add(a5)
    c5 = b5[0:5]
    # print(add(a5))  # c5 Profile short/long Type 1/2/4/7/9
    a6 = hex2bin(s6)
    b6 = add(a6)
    # print("b6 ::::", b6)
    c6 = b6[2:9]  # c6: path id
    # print("c6 :::::", c6)
    # print(add(a6))
    a7 = hex2bin(s7)
    b7 = add(a7)
    # print(b7)
    # print(add(a7))
    a8 = hex2bin(s8)
    a8 = add(a8)
    b8 = a8[3:9]
    c8 = b8 + b7  # c8: offset
    offset = bin2dec(c8)
    path_id = bin2dec(c6)
    ProfType = bin2dec(c5)
    t2.insert(END, offset)
    t3.insert(END, path_id)
    t4.insert(END, ProfType)
    # print("offset : ", bin2dec(c8))
    # print("path id : ", bin2dec(c6))
    # print("ProfType : ", bin2dec(c5))


offset, path_id, ProfType = "", "", ""
main_window = Tk()
main_window.title("resolve")

l1 = Label(main_window, height=1, width=25, text="Please Input HEX Number:").grid(row=0, column=0)
E1 = Entry(main_window, width=25)
E1.grid(row=0, column=1)

l2 = Label(main_window, height=1, width=25, text="offset:").grid(row=1, column=0)
t2 = Text(main_window, height=1, width=25)
t2.grid(row=1, column=1)

l3 = Label(main_window, height=1, width=25, text="Path id:").grid(row=2, column=0)
t3 = Text(main_window, height=1, width=25)
t3.grid(row=2, column=1)

l4 = Label(main_window, height=1, width=25, text="Profile_Type:").grid(row=3, column=0)
t4 = Text(main_window, height=1, width=25)
t4.grid(row=3, column=1)

b1 = Button(main_window, text="okay", command=calc)
b1.grid(row=4, column=1)

main_window.mainloop()