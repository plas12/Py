'''
f = open("example.txt", "w")
f.close()
 

f = open("example.txt", "w")
for i in range(1, 4):
    f.write("Line %d\n" % i)
f.close()


f = open("example.txt", "a")
alphabet = ['A', 'B', 'C', 'D', 'E']

for c in alphabet:
    f.write(c)
f.close()


f = open("example.txt", "r")
data = f.read()
print(data)
f.close()


f = open("example.txt", "r")
while (1):
    line = f.readline()
    if not line: break#not line은 line이 없을때
    print(line, end = '')
f.close()


f = open("example.txt", "r")
data = f.readlines()
for line in data:
    print(line, end = '')
f.close()


f = open("example.txt", "r")
while True:
    print(f.tell(), end = ' ')
    line = f.readline()
    print(line.strip())
    if not line: break
f.seek(26)
print("after setting a pointer : %d(%s)" % (f.tell(), f.read()[0]))#26번 부터 0번째의 위치
f.close()


f = open("profile.txt", "w")
name = input("Name : ")
age = input("Age : ")
f.write("Name : %s\n" % name)
f.write("Age : %s\n" % age)
f.close()


f = open("profile.txt", "w")
a = [input("Name : "), input("Age : "), input("School : ")]
b = ["Name", "Age", "School"]
for i in range(3):
    f.write("%s : %s\n" %(b[i], a[i]))
f.close()


f = open("profile.txt", "r")
while True:
    line = f.readline()
    print(line, end = '')
    if not line: break

f.close()


f = open("profile.txt", "r")
data = f.readlines()
for i in range(3):
    print(data[i], end = '')
f.close()


from tkinter import *

def get_click():
    lbl2["text"] = txt_box.get(1.0, END)

def ins_click():
    txt_box.insert(1.0, lbl1["text"])

def del_click():
    txt_box.delete(1.0, END)

win = Tk()
txt_box = Text(win, width = 40, height = 5)

lbl1 = Label(win, text = "Click the 'insert' button to insert this string.", width = 40, height = 5, bg = "skyblue")

lbl2 = Label(win, text = "Click the 'get' button to import textbox steings\ninto this label.", width = 40, height = 5, bg = "pink")

btn_get = Button(win, text = "get", width = 10, command = get_click)
btn_ins = Button(win, text = "insert", width = 10, command = ins_click)
btn_del = Button(win, text = "delete", width = 10, command = del_click)

txt_box.grid(row = 0, column = 0, columnspan = 3)
lbl1.grid(row = 1, column = 0, columnspan = 3)
lbl2.grid(row = 2, column = 0, columnspan = 3)
btn_get.grid(row = 3, column = 0)
btn_ins.grid(row = 3, column = 1)
btn_del.grid(row = 3, column = 2)

win.mainloop()


f = open("fruit.txt", "w")
txt = ["apple", "banana", "orange", "grape", "kiwi", "strawberry", "wildberry", "watermelon", "mange", "papaya", "coconut"]
for i in range( len( txt)):
    f.write("%s\n" % txt[i])
f.close

f = open("fruit.txt", "r")
#파일 읽어오기
n = f.read()
n = n.split("\n")
print(n)
#기준 정하기
b = int(input())
#길이 구하기
for i in n:
  if len(i) > b:
    print(i)

f.close()
#길이 구하기


#f = open("anna.txt", "w")
#f.write("Elsa? Do you want to build a snowman?\nCome on, let's go and play! i naver see you\nanymore Come out the door it's like you've\ngone away We used to be best buddies And\nnow we're not i wish you would tell me wht?\nDo you want to build a snowman? it doesn't\nhave to be a snowman Go away, Anna Okay\nbye")
#f.close()

f = open("anna.txt", "r")
n = f.read()
n = n.split()
for i in n:
  if i.count('b') > 0:
    print(i)
    
    
f.close()
