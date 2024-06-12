'''
def times(n):
    for i in range(1, 10):
        print("%d * %d = %d" %(n, i, n * i), end = '\n')
a = int(input())
times(a)


a = 59
b = 15
def asdf():
    global a
    a = 10
    print(a)
    b = 10
    print(b)
asdf()
print(a)
print(b)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
fac = factorial(4)
print(fac)


def judge(n):
    if( n > 0 ):
        print("plus")
    elif( n < 0 ):
        print("minus")
    else:
        print("zero")
judge(int(input()))


def season(n):
    if(2 < n
    and n < 6):
        print("spring")
    if(5 < n and n < 9):
        print("summer")
    if(8 < n and n < 12):
        print("fail")
    if(11 < n or n < 3):
        print("winter")
season(int(input()))


from random import*

def lotto():
    lot = []
    for i in range(6):
        lot.append(randint(1, 45))
        
    lot.sort()
    print(lot)
    
lotto()


from random import*

def lotto():
    lot = []

    while len(lot) < 6:
        num = randint(1, 45)
        if num not in lot:
            lot.append(num)
        
    lot.sort()
    print(lot)
    
lotto()


def point(n):
    a = 1
    for i in range(len(n)):
        if(a == 0):
            print(n[i], end = '')
        if(n[i] == '.'):
            a = 0
point(input())   


def f(n):
    a = 1
    for i in range(n):
        for j in range(1, n + 1):
            print(j * a, end = ' ')
        print()
        a += 1
f(int(input()))
'''

a = []
b = 0
c = 0
d = 0

while(1):
    num = int(input())
    if(num == -1):
        break
    a.append(num)
    b += 1

def total(a, b):
    tt = 0
    for i in range(len(a)):
        tt += a[i]
    return tt
c = total(a, b)

def average(c, b):
    a = c / b
    return a
d = average(c, b)

for i in range(len(a)):
    
