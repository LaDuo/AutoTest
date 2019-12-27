import PySimpleGUI as sg

sg.change_look_and_feel("DarkBlue")

# ---------- Menu Definition ----------- #
menu_def = [['&File', ['&Open', '&Save', '&Exit', 'Propertes']],
            ['&Edit', ['Pase', ['Special', 'Normal', ], 'Undo']],
            ['&Help', 'About...']
            ]

frame1_layout = [
    [sg.Text("将Av2_Input文件夹中的log合并至Av2_Output", auto_size_text=True),
     sg.Button(button_text="Get", button_color=('black', 'blue'), pad=(20, 3), size=(10, 1))],
    [sg.Text("从outfile.txt中提取六种消息", auto_size_text=True),
     sg.Button(button_text="Get", button_color=('black', 'blue'), pad=(120, 3), size=(10, 1))],
    [sg.Text("将Ehplog中的ehp和localization的INFO文件合并", auto_size_text=True),
     sg.Button(button_text="Get", button_color=('black', 'blue'), size=(10, 1))],
    [sg.Text("提取matchpt和gcj", auto_size_text=True),
     sg.Button(button_text="Get", button_color=('black', 'blue'), pad=(175, 3), size=(10, 1))],
    # [sg.Open()]
]

frame2_layout = [
    [sg.Text("判断position消息的offset是否递增", auto_size_text=True),
     sg.Button(button_text="Get", button_color=('black', 'blue'), pad=(80, 3), size=(10, 1))],
    [sg.Text("判断stub消息的offset是否递增", auto_size_text=True),
     sg.Button(button_text="Get", button_color=('black', 'blue'), pad=(100, 3), size=(10, 1))],
    [sg.Text("判断stub消息在重构时是否发送", auto_size_text=True),
     sg.Button(button_text="Get", button_color=('black', 'blue'), pad=(93, 3), size=(10, 1))],
    [sg.Text("判断segment消息是否重发", auto_size_text=True),
     sg.Button(button_text="Get", button_color=('black', 'blue'), pad=(120, 3), size=(10, 1))],
    [sg.Text("判断各个消息是否丢包", auto_size_text=True),
     sg.Button(button_text="Get", button_color=('black', 'blue'), pad=(144, 3), size=(10, 1))]
]

frame3_layout = [
    [sg.T("Some ohter action ", auto_size_text=True)],
    [sg.Text("生成Issue状态报表", auto_size_text=True),
     sg.Button(button_text="Do it", button_color=('black', 'blue'), pad=(173, 3), size=(10, 1))],
    [sg.Text("删除无用的log", auto_size_text=True),
     sg.Button(button_text="Delete it", button_color=('black', 'blue'), pad=(200, 3), size=(10, 1))],
    [sg.Text("按照offset和path id的规则来显示slope", auto_size_text=True)],
    [sg.CB("mode 2"), sg.CB("mode 3"),
     sg.Button(button_text="Show it", button_color=('black', 'blue'), pad=(135, 3), size=(10, 1))],
]
# main layout
layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('请输入回放的路线名 :', auto_size_text=True), sg.InputText(key='-IN-'),
     sg.Button(button_text="创建文件夹", button_color=('black', 'blue'), size=(10, 1))],
    [sg.Frame('操作 Log', frame1_layout, font='Any 12', title_color='blue', title_location='n'),
     sg.Frame('判断 Log', frame2_layout, font='Any 12', title_color='blue', title_location='n')],
    [sg.Frame("Action", frame3_layout, font='Any 12', title_color='blue', title_location='n')]
]

window = sg.Window('Hello World!', layout, default_element_size=(40, 1), grab_anywhere=False)

while True:
    event, values = window.read()
    if event in (None, 'exit'):
        break
    if event in 'create':
        print("I got you")

window.close()
