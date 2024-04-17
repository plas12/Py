'''
i = 1
while(i <= 10):
    print(i, end = ' ')
    i+=1


sum = 0
i = 1
while(i <= 100):
    sum += i
    i +=1
print(sum)


i = 0
while(i < 10):
    i += 1
    if(i % 2 == 0):
        continue
    print(i, end = ' ')


while(1):
    ans = input("Shall we close (y/n)")
    if(ans == 'y'):
        print("The end")
        break


stamp = 0
while(stamp < 10):
    stamp += 1
    print("스탬프 %d개 적립" %stamp)
    if(stamp == 10):
        print("무료 음료 쿠폰 1개 증정")


a = int(input())
b = 0
c = 0
while(b < a):
    b += 1
    c += b
print(c)


a = int(input())
b = int(input())
c = b
while(b < a):
    b += 1
    c += b
print(c)


a = 1
b = 0
c = 0
while(a != 0):
    a = int(input())
    b += a
    c += 1
print(b / c)


a = int(input())
b = 0
while(a > 0):
    a = a // 10
    b += 1
print(b,"자리수")
'''


a = int(input())
ab = a
b = 10
c = 0
#while(ab > 1):
#    ab = ab // 10
#    b *= 10
#print(a)
#b /= 10
while(a > 1):
    print("!")
    c = a % b
    a = a - c
    a = a / 10
    print(c)
    b *= 10

