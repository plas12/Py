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
'''

