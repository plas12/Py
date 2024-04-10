'''
x = True
y = False
print('x : %s, y : %s' % (x, y))
print('x and y = ', x and y)
print('x or y =', x or y)
print('not x = ', not x)
print('not y =', not y)


score = int(input())
if(score >= 60 and score <= 100):
    print("Pass")
else:
    print("Fall")


score = int(input())
if (score >= 90):
    print('A')
elif (score >= 60):
    print('B')
else:
    print('C')


score = int(input())
if(score >= 90):
    print('A')
else:
    if(score >= 60 and score <=89):
        print('B')


a = int(input())
b = int(input())
c = int(input())
print(140 <= a and 140 <= b and 140 <= c)


a = int(input())
if(a % 2 == 0):
    print('EVEN')
else:
    print('OOO')


y = int(input())
if(y % 4 == 0 and y % 100 != 0 or y % 400 == 0):
    print('leap year')
else:
    print('common year')


a = 1 in (1, 2, 3)
print(a)
a = 1 not in[1, 2, 3]
print(a)


case = ['Homework', 'Eating', 'Sleeping']
if('Homework' in case):
    print(' I have to do Homework')
else:
    print("It%'s break time")


a = input()
if(a == 'M'):
    print("man")
elif(a == 'W'):
    print("woman")
else:
    print("what")


a = int(input())
if(1 <= a and a <= 6):
    print("first half")
else:
    print("second half")


import random
com = random.randint(1, 2)#(이상 , 이하)
user = int(input('odd : 1, even : 2\n'))
print("COM(%d) : USER(%d)" %(com, user))
if(com == user):
    print("Correct")
else:
    print("Incorrect")


import random
com = random.randint(1, 3)
user = int(input("가위 : 1, 바위 : 2, 보자기 : 3\n"))
print("COM(%d) : USER(%d)" %(com, user))
if(com == user):
    print("비김")
if(com == 1 and user == 2):
    print("이김")
if(com == 2 and user == 3):
    print("이김")
if(com == 3 and user == 1):
    print("이김")
if(com == 1 and user == 3):
    print("짐")
if(com == 2 and user == 1):
    print("짐")
if(com == 3 and user == 2):
    print("짐")
'''

import random
a1 = 0
a2 = 0
b1 = 0
b2 = 0
input("1p : 주사위를 돌릴려면 enter키를 누르시오")
a1 = random.randint(1, 6)
input("2p : 주사위를 돌릴려면 enter키를 누르시오")
b1 = random.randint(1, 6)
input("결과를 보려면 enter키를 누르시오")
print("첫번째 주사위 결과")
print("1p(%d) : 2p(%d)" %(a1, b1))
print("\n")
input("1p : 주사위를 돌릴려면 enter키를 누르시오")
a2 = random.randint(1, 6)
input("2p : 주사위를 돌릴려면 enter키를 누르시오")
b2 = random.randint(1, 6)
input("결과를 보려면 enter키를 누르시오")
print("두번째 주사위 결과")
print("1p(%d) : 2p(%d)" %(a2, b2))
print("\n")
print("== 경기 결과 ==")
print("1p : (%d) / 2p : (%d)" %(a1 + a2, b1 + b2))
if(a1 + a1 < b1 + b2):
    print("2p 승!")
elif(a1 + a2 > b1 + b2):
    print("1p 승!")
else:
    print("비김")
