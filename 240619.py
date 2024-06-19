'''
#import tkinter#함수중 일부

from tkinter import*#전체 함수

win = Tk()
win.title("C3 coding")
win.geometry("300x200+100+100")#+100+100은 컴퓨터 모니터의 좌표(그곳에 윈도우 창을 생성한다는 뜻)
win.resizable(True, False)
win.mainloop()


from tkinter import*

win = Tk()
label1 = Label(win, text = "one")
label2 = Label(win, text = "two")
label3 = Label(win, text = "three")
label1.pack()
label2.pack()
label3.pack()
win.mainloop()


from tkinter import*

win = Tk()
lbl1 = Label(win, text = "orange", width = 20, height = 3, relief = "solid")
lbl2 = Label(win, text = "banana", font = ("Elephant", 20), bg = "yellow")
lbl3 = Label(win, text = "apple", fg = "red")

lbl1.pack()
lbl2.pack()
lbl3.pack()
win.mainloop()


from tkinter import*

win = Tk()
List = ["info", "warning", "error", "question", "questhead", "hourglass", "gray12", "gray25", "gray50", "gray75"]
for i in range(10):
    lbl = Label(win, bitmap = List[i])
    lbl.pack(side = "left") 


from tkinter import*
from PIL import ImageTk

win = Tk()

img = ImageTk.PhotoImage(file = "타코.png")
lbl = Label(win, image = img)
lbl.pack()
win.mainloop()


from tkinter import*

win = Tk()
btn = Button(win, text = "Button")
btn.pack()
win.mainloop()


from tkinter import*

win = Tk()

def click():
    if(btn['text'] == "red"):
        btn['text'] = "blue"
        btn['bg'] = "blue"
    else:
        btn['text'] = "red"
        btn['bg'] = "red"
btn = Button(win, text = "red", fg = "white", bg = "red", command = click)
btn.pack()
win.mainloop()


from tkinter import*

win = Tk()

def click():
    if(lbl['text'] == "hello"):
        lbl['text'] = "python"
        lbl['bg'] = "green"
    else:
        lbl['text'] = "hello"
        lbl['bg'] = "orange"
lbl = Label(win, text = "hello", fg = "white", bg = "orange")
btn = Button(win, text = "Button", fg = "black", bg = "white", command = click)
btn.pack()
lbl.pack()
win.mainloop()


from tkinter import*

win = Tk()

def message(event):
    lbl['text'] = entry.get()
entry = Entry(win)
entry.bind("<Return>", message)
entry.pack()
lbl = Label(win, text = "")
lbl.pack()
win.mainloop()


from tkinter import*

win = Tk()
a = 0

def add(event):
    global a
    a = a + int(entry.get())
    lbl['text'] = a
    entry.delete(0, END)

def click():
    global a
    a = 0
    lbl['text'] = "0"
    
entry = Entry(win)
entry.bind("<Return>", add)
lbl = Label(win, text = "")
btn = Button(win, text = "clear", fg = "black", bg = "white", command = click)
lbl.pack()
entry.pack()
btn.pack()
win.mainloop()
'''

from tkinter import*

win = Tk()

def click1():
    lable_txt['text'] = "red"
def click2():
    lable_txt['text'] = "orange"
def click3():
    lable_txt['text'] = "yellow"
def click4():
    lable_txt['text'] = "green"
def click5():
    lable_txt['text'] = "blue"
def click6():
    lable_txt['text'] = "black"

btn1 = Button(win, text = "", bg = "red", fg = "red", width = 10, height = 5, command = click1)
btn2 = Button(win, text = "", bg = "orange", fg = "orange", width = 10, height = 5, command = click2)
btn3 = Button(win, text = "", bg = "yellow", fg = "yellow", width = 10, height = 5, command = click3)
btn4 = Button(win, text = "", bg = "green", fg = "green", width = 10, height = 5, command = click4)
btn5 = Button(win, text = "", bg = "blue", fg = "blue", width = 10, height = 5, command = click5)
btn6 = Button(win, text = "", bg = "black", fg = "black", width = 10, height = 5, command = click6)
lable_txt = Label(win, text = "")

lable_txt.grid(row =0, column = 1)
btn1.grid(row =1, column = 0)
btn2.grid(row =1, column = 1)
btn3.grid(row =1, column = 2)
btn4.grid(row =2, column = 0)
btn5.grid(row =2, column = 1)
btn6.grid(row =2, column = 2)
