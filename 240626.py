'''
add = lambda x, y : x + y
print(add(int(input()), int(input())))


remains = lambda a, b : a % b
print(remains(int(input()), int(input())))
      

say = lambda name : print("Hello", name)
say(input())


from tkinter import *

def Click(n):
    if n == 1:
        lbl['text'] = "First button clicked."
    elif n == 2:
        lbl['text'] = "Second button clicked."
    else:
        lbl['text'] = "Third button clicked."

win = Tk()
lbl = Label(win, text = "이름")

btn1 = Button(win, text = "First", command = lambda : Click(1))#command의 뒤에 함수를 쓸때 변수를 넣는다면 (click(1)에서의 1) 앞에 lambda를 써야 된다.
btn2 = Button(win, text = "Second", command = lambda : Click(2))
btn3 = Button(win, text = "Third", command = lambda : Click(3))

lbl.grid(row = 0, column = 0, columnspan = 3)
btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 1, column = 2)
win.mainloop()


from tkinter import *

def Click(shape):
    if shape == "circle":
        img = PhotoImage(file = "circle.png")
    elif shape == "triangle":
        img = PhotoImage(file = "triangle.png")
    else:
        img = PhotoImage(file = "star.png")
    lbl['image'] = img
    lbl.image = img

win = Tk()
img = PhotoImage(file = "circle.png")
lbl = Label(win, image = img)
btn1 = Button(win, text = "circle", command = lambda : Click("circle"))
btn2 = Button(win, text = "triangle", command = lambda : Click("triangle"))
btn3 = Button(win, text = "star", command = lambda : Click("star"))

lbl.grid(row = 0, column = 0, columnspan = 3)
btn1.grid(row = 1, column = 0)
btn2.grid(row = 1, column = 1)
btn3.grid(row = 1, column = 2)
win.mainloop()
'''

from tkinter import *
from PIL import ImageTk
from random import *

win = Tk()
win.title("Rock Paper Scissors Game")

def change_img(user):
    List = ["scissors.png", "rock.png", "paper.png"]
    com = randint(0, 2)

    com_img = PhotoImage(file = List[com])
    user_img = PhotoImage(file = List[user])
    print(List[user])
    print(List[com])
    
    lbl_user['image'] = user_img
    lbl_com['image'] = com_img

    lbl_user.image = user_img
    lbl_com.image= com_img

    game(user, com)

def game(user, com):
    rex_txt = ''
    
    if(user == 0 ):
        if(com == 0):
            res_txt = 'draw'
        elif(com == 1):
            res_txt = 'lose'
        else:
            res_txt = 'win'
    if(user == 1 ):
        if(com == 0):
            res_txt = 'win'
        elif(com == 1):
            res_txt = 'draw'
        else:
            res_txt = 'lose'
    if(user == 2 ):
        if(com == 0):
            res_txt = 'lose'
        elif(com == 1):
            res_txt = 'win'
        else:
            res_txt = 'draw'
    lbl_res['text'] = res_txt
    lbl_res.text = res_txt

basic_img = ImageTk.PhotoImage(file = 'ready.png')

lbl_com = Label(win, image = basic_img, relief = "solid")
lbl_user = Label(win, image = basic_img, relief = "solid")

lbl_res = Label(win, text = '', width = 15, font = ("consolas", 20, "bold"), fg = "brown", bg = "lightyellow")

lbl_name1 = Label(win, text = 'user', font = ("consolas", 20))
lbl_name2 = Label(win, text = 'com', font = ("consolas", 20))

btn_scissor = Button(win, text = 'scissor', width = 15, font = ("consolas", 15), bg = "skyblue", command = lambda : change_img(0))
btn_rock = Button(win, text = 'rock', width = 15, font = ("consolas", 15), bg = "pink", command = lambda : change_img(1))
btn_paper = Button(win, text = 'paper', width = 15, font = ("consolas", 15), bg = "light green", command = lambda : change_img(2))

lbl_user.grid(row = 0, column = 0)
lbl_res.grid(row = 0, column = 1)
lbl_com.grid(row = 0, column = 2)
lbl_name1.grid(row = 1, column = 0)
lbl_name2.grid(row = 1, column = 2)
btn_scissor.grid(row = 2, column = 0)
btn_rock.grid(row = 2, column = 1)
btn_paper.grid(row = 2, column = 2)

win.mainloop()
