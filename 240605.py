'''
def add(x, y):
    s = x + y
    return s
result = add(10, 20) + add(20, 30)
print(result)


def f(n):
    n = 20
    return n
n = 10

f(n)
print(n)

n = f(n)
print(n)


def get_max(x, y):
    if(x > y):
        return x
    else:
        return y

a = int(input())
b = int(input())

max = get_max(a, b)

print(max)


def plus(x):
    if(x < 0):
        return False
    else:
        return True

a = int(input())

print(plus(a))


def get_sum(x):
    a = 0
    for i in range(x + 1):
        a += i
    return a
b = int(input())

print("1부터 ", b, " 까지의 합은 ", get_sum(b), "입니다")


def get_sum(x, y):
    a = 0
    for i in range(x, y + 1):
        a += i
    return a

a = int(input())
b = int(input())
print(a,"부터 ", b,"까지의 합은 ",get_sum(a, b),"입니다.")


def number(n):
    if(n % 2 == 0):
        return 'even'
    return 'odd'
a = int(input())
print(number(a))


def square(x, y):
    a = 1
    for i in range(y):
        a *= x
    return a
a = int(input())
b = int(input())
print(square(a, b))


def get_sum(n):
    a = 0
    for i in range(n):
        b = int(input())
        a += b
    return a
a = int(input())
print(get_sum(a))


def get_max(n):
    a = 0
    b = 0
    for i in range(n):
        b = int(input())
        if(a < b):
            a = b
    return a
a = int(input())
print(get_max(a))


def is_prime(n):
    a = 0
    for i in range(1, n + 1):
        if(n % i == 0):
            a += 1
    if(a == 2):
        return 1
    return 0

a = int(input())
b = 0
for i in range(1, a + 1):
    if(is_prime(i) == 1):
        print(i, end = ' ')


def is_prime(n):
    for i in range(2, n):
        if(n % i == 0):
            return 0
    return 1

a = int(input())

for i in range(2, a + 1):
    if(is_prime(i) == 1):
        print(i, end = ' ')
'''

def find_index(str1, ex):
    a = []
    for i in range(len(str1)):
        if(str1[i] == ex):
            a.append(i)
    return a

str1 = input()
ex = input()

print(find_index(str1, ex))
