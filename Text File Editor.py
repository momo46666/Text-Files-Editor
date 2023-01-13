import tkinter as tk  #导入各种的库，主要是TKinter，一个GUI库
import time            #一个时间库
from tkinter import *
import datetime        #为了后面获取当前日期用的库

import webbrowser

window = tk.Tk()
window.title("TFE")
window.geometry("500x500")
menubar = tk.Menu(window)
text1 = "Text File Editor\nA Good Editor"

name_input = Text(window, width="60", height="35")   #文本框
name_input.pack()

def txr(ti, tex):
    window = tk.Tk()
    window.title(ti)
    window.geometry("500x300")
    name_input = Text(window, width="60", height="35")
    name_input.pack()
    name_input.insert(tk.END, tex)

def tx():               #help后的文本框
    window = tk.Tk()
    window.title("关于TFE")
    window.geometry("500x300")
    name_input = Text(window, width="60", height="35")
    name_input.pack()
    name_input.insert(tk.END, "注意事项：\n1.打开文件时需保证需打开文件名为“new file.txt”,且与exe文件在同一目录下\n制作者：落地水的末末")


def win():          #help后的界面
    window = tk.Tk()
    window.title("关于TFE")
    window.geometry("250x300")
    menubar = tk.Menu(window)
    lb = tk.Label(window,text=text1,width=30,height=14,justify="left",anchor="nw",fg="black",bg="white",padx=0,pady=10,)
    lb.pack()
    tk.Button(window, width=10, height=1, text="相关", command=tx).pack()


def openf():
    mfile = open("new file.txt", "r")  # 打开文件
    name_input.insert(tk.END, mfile.read())  # 将打开的文件插入文本框
    mfile.close()  # 关闭文件


def text_create(name, msg):
    desktop_path = "C:\\Users\\Administrator\\Desktop\\"  # 新创建的txt文件的存放位置
    full_path = desktop_path + name + ".txt"  # 文件名和后缀名
    file = open(full_path, "w")
    file.write(msg)
    file.close()  # 关闭文件

def getTextInput():
    result = name_input.get("1.0", "end")  # 获取文本输入框的内容
    text_create("new file", result)  # 生成文件

def gettime():   #获取当前时间
    now_time=datetime.date.today()   #获取时间
    name_input.insert(tk.END, now_time)   #将获取时间插入文本框

def exi():
    window = tk.Tk()    #关于无法退出的解释界面
    window.title("退出")
    window.geometry("250x300")
    menubar = tk.Menu(window)
    lb = tk.Label(window,text='由于一些特殊原因所致的错误\n请点右侧的退出按钮',width=30,height=14,justify="left",anchor="nw",fg="black",bg="white",padx=0,pady=10,)
    lb.pack()
    tk.Button(window, width=10, height=1, text="抱歉").pack()

def openweb():
    webbrowser.open('https://space.bilibili.com/3461567521753656?spm_id_from=333.1007.0.0')

editmenu3 = tk.Menu(menubar, tearoff=False)
editmenu2 = tk.Menu(menubar, tearoff=False)
editmenu1 = tk.Menu(menubar, tearoff=False)
editmenu = tk.Menu(menubar, tearoff=False)
# ----------------------------------以下为文件
editmenu.add_command(label="打开文件", command=openf)
editmenu.add_command(label="保存", command=getTextInput)
editmenu.add_command(label="退出",command=exi)
menubar.add_cascade(label="文件", menu=editmenu)
# ---------------------------------以下为编辑
editmenu1.add_command(label="日期", command=gettime)
menubar.add_cascade(label="编辑", menu=editmenu1)
# ---------------------------------以下为帮助
editmenu3.add_command(label="关于TFE", command=win)
menubar.add_cascade(label="帮助", menu=editmenu3)
# ---------------------------------以下为设置
editmenu2.add_command(label="详情",command=openweb)
menubar.add_cascade(label="作者", menu=editmenu2)
# 显示菜单
window.config(menu=menubar)

window.mainloop()


