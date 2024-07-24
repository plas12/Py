''' 
from tkinter import *

win = Tk()
listbox = Listbox(win)
for i in range(10):
listbox.insert(i, str(i))
print(listbox.curselection())
print(listbox.get(0, 9))
listbox.pack()
win.mainloop()


from tkinter import *

def double_click(event):
index = listbox.curselection()#클릭한 거에서 확인한다.
print("Today :", listbox.get(index[0]))

def left_click(event):
index = listbox.curselection()
if index:
    if index[0] == 0:
        print("Yesterday : Sun")
    else:
        print("Yesterday :", listbox.get(index[0] - 1))

def right_click(event):
index = listbox.curselection()
if index:
    if index[0] == 6:
        print("Tomorrow : Mon")
    else:
        print("Tomorrow :", listbox.get(index[0] + 1))

day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

win = Tk()

listbox = Listbox(win)

for i in range(7):
listbox.insert(i, day[i])
listbox.bind("<Double-Button-1>", double_click)
listbox.bind("<Button-1>", left_click)
listbox.bind("<Button-3>", right_click)

listbox.pack()
win.mainloop()


from tkinter import *

def double_click(event):
index = listbox.curselection()
label['text'] = listbox.get(index[0])

win = Tk()
label = Label(win, text = '', bg = 'pink')
listbox = Listbox(win)

flower = ["rose", "lily", "pansy", "sunflower"]

for i in range(4):
listbox.insert(i,  flower[i])
listbox.bind("<Double-Button-1>", double_click)

label.pack()
listbox.pack()
win.mainloop()


from datetime import datetime

print(datetime.today())
print(datetime.now())


from datetime import datetime

print(datetime.today().strftime("%Y년 %m월 %d일"))
print(datetime.today().strftime("%H시 %M분"))
print(datetime.today().strftime("%Y/%m/%d  %H:%M:%S"))


from tkinter import *
win = Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 100)
canvas.create_line(0, 50, 500, 50, fill = "blue", width = 5)
canvas.pack()
win.mainloop()


from tkinter import *

win = Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 100)
canvas.pack()

x1, y1 = 0, 0
x2, y2 = 500, 0

for i in range(3):
y1 += 30
y2 = y1
canvas.create_line(x1, y1, x2, y2, fill = "red", width = 3)

win.mainloop()


from tkinter import *

win = Tk()
canvas = Canvas(win, bg = "white", width = 470, height = 470)
canvas.pack()

x1, y1 = 10, 10
x2, y2 = 460, 10
canvas.create_line(x1, y1, x2, y2, fill = "blue", width = 3)
for i in range(9):
y1 += 50
y2 =y1
canvas.create_line(x1, y1, x2, y2, fill = "blue", width = 3)

x1, y1 = 10, 10
x2, y2 = 10, 460
canvas.create_line(x1, y1, x2, y2, fill = "red", width = 3)
for i in range(9):
x1 += 50
x2 =x1
canvas.create_line(x1, y1, x2, y2, fill = "red", width = 3)


from tkinter import *

def paint(event):
    x1, y1 = event.x , event.y
    x2, y2 = x1 + 5, y1 + 5
    canvas.create_line(x1, y1, x2, y2, width = 3)

win = Tk()
canvas = Canvas(win, bg = "white", width = 500, height = 200)
canvas.pack()

win.bind('<B1-Motion>', paint)

win.mainloop()
'''

from tkinter import *

pen_color = "black"

def paint(event):
    global pen_color
    x1, y1 = event.x, event.y
    x2, y2 = x1 + 5, y1 + 5
    canvas.create_line(x1, y1, x2, y2, width = 3, fill = pen_color)

def change_color():
    global pen_color
    pen_color = "red"

win = Tk()
canvas = Canvas(win, bg = "white", width = 500 , height = 200)
btn = Button(win, text = "red", command = change_color)
canvas.pack()
btn.pack()

win.bind("<B1-Motion>", paint)
win.mainloop()
