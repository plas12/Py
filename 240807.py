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
'''
'''
from tkinter import *

win = Tk()
canvas = Canvas(win, width = 200, height = 100, bg = "white")
canvas.pack()

canvas.create_oval(10, 10, 60, 60, fill = "blue")#타원

canvas.create_rectangle(100, 10, 160, 60, fill = "yellow", outline = "red")#직사각형

win.mainloop()
'''
'''
from tkinter import *

win = Tk()
canvas = Canvas(win, width = 200, height = 100, bg = "white")
canvas.pack()

canvas.create_polygon(100, 10, 30, 90, 160, 90, fill = "red")

win.mainloop()
'''
'''
from tkinter import *
from random import *
def draw_shape(event):
    color = ["black", "white", "blue", "red", "green", "yellow"]
    x1, y1 = event.x, event.y
    x2, y2 = x1 + randint(10, 70), y1 + randint(10, 70)
    canvas.create_rectangle(x1, y1, x2, y2, fill = color[randint(0, 5)])

win = Tk()
canvas = Canvas(win, width = 300, height = 300, bg = "white")
canvas.pack()
canvas.bind("<Double-Button-1>", draw_shape)

win.mainloop()
'''

from tkinter import *

win = Tk()

pen_color = "black"
pen_size = 2
shape_size = 10
my_tool = "pen"
fill_color = "white"
color = ["black", "blue", "green", "white", "red", "yellow"]

w, h = 13, 2

win.geometry("510x600+200+200")


def paint(event):
    global pen_color, pen_size
    x1, y1 = event.x, event.y
    x2, y2 = x1 + pen_size, y1 + pen_size
    canvas.create_line(x1, y1, x2, y2, width = 3, fill = pen_color)

def change_color(color):
    global pen_color, fill_color, my_tool
    if my_tool == "pen":
        pen_color = color
        btnpc['bg'] = color
        if color =="white" or color == "yellow":
            btnpc['fg'] == "black"
        elif color == "black":
            btnpc['fg'] = "white"
    elif my_tool == "canvas":
        canvas['bg'] = color
        btncc['bg'] = color
        if color =="white" or color == "yellow":
            btncc['fg'] == "black"
        elif color == "black":
            btncc['fg'] = "white"
    else:
        fill_color = color
        btnfc['bg'] = color
        if color =="white" or color == "yellow":
            btnfc['fg'] == "black"
        elif color == "black":
            btnfc['fg'] = "white"

def change_size(btn):
    global shape_size, pen_size, my_tool
    if my_tool == "pen":
        if btn == "P":
            pen_size += 1
        if btn == "M" and pen_size > 2:
            pen_size -= 1
    else:
        if btn == "P":
            shape_size += 10
        if btn == "M" and shape_size > 10:
            shape_size -= 10

def change_tool(tool):
    global my_tool
    my_tool = tool
    print(my_tool)

def clear():
    canvas['bg'] = "white"
    btncc['bg'] = "white"
    btncc['fg'] = "black"
    canvas.delete("all")

def draw_shape(event):
    global shape_size, my_tool
    x1, y1 = event.x, event.y
    x2, y2 = event.x + shape_size, event.y + whape_size
    if my_tool == "oval":
        canvas.create_oval(x1 - (shape_size / 2), y1, x2
        

canvas = Canvas(win, bg = "white", width = 510 , height = 470)
btn1 = Button(win, text = color[0], bg = "black",  fg = "white", width = w , height = h, command = lambda : change_color(color[0]))
btn2 = Button(win, text = color[1], bg = "blue",  fg = "white", width = w , height = h, command = lambda : change_color(color[1]))
btn3 = Button(win, text = color[2], bg = "green",  fg = "white", width = w , height = h, command = lambda : change_color(color[2]))
btn4 = Button(win, text = color[3], bg = "white",  fg = "black", width = w , height = h, command = lambda : change_color(color[3]))
btn5 = Button(win, text = color[4], bg = "red",  fg = "white", width = w , height = h, command = lambda : change_color(color[4]))
btn6 = Button(win, text = color[5], bg = "yellow", fg = "white", width = w , height = h, command = lambda : change_color(color[5]))
btnc = Button(win, text = "○", width = w , height = h)
btnr = Button(win, text = "□", width = w , height = h) 
btnp = Button(win, text = "△", width = w , height = h)
btncc = Button(win, text = "canvas\nclolr", width = w , height = h, command = lambda : change_tool("canvas"))
btnpc = Button(win, text = "pen\ncolor", width = w , height = h, command = lambda : change_tool("pen"))
btnfc = Button(win, text = "fill\ncolor", width = w , height = h, command = lambda : change_tool("fill"))
btnP = Button(win, text = "+", width = w , height = h, command = lambda : change_size("P"))
btnM = Button(win, text = "-", width = w , height = h, command = lambda : change_size("M"))
btnD = Button(win, text = "clear", width = w , height = h, command = clear)

canvas.grid(row = 0, column = 0, columnspan = 5)
btncc.grid(row = 1, column = 0)
btnpc.grid(row = 2, column = 0)
btnfc.grid(row = 3, column = 0)
btn1.grid(row = 1, column = 1)
btn2.grid(row = 1, column = 2)
btn3.grid(row = 1, column = 3)
btn4.grid(row = 2, column = 1)
btn5.grid(row = 2, column = 2)
btn6.grid(row = 2, column = 3)
btnc.grid(row = 3, column = 1)
btnr.grid(row = 3, column = 2)
btnp.grid(row = 3, column = 3)
btnP.grid(row = 1, column = 4)
btnM.grid(row = 2, column = 4)
btnD.grid(row = 3, column = 4)


win.bind("<B1-Motion>", paint)
win.mainloop()
