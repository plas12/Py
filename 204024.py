'''
List = ['a','b','c','d','e','f','g']
for s in List:
    print(s)


num_list = [1, 2, 3, 4, 5]
sum = 0
for num in num_list:
    sum += num
print("avg : %d" %(sum//5))


aList = [1, 2, 3]
bList = [10, 100, 1000]
for a in aList:
    for b in bList:
        print(a * b, end = ' ')
    print()


for i in range(10):
    print(i, end = ' ')
print()
for i in range(10, 21):
    print(i, end = ' ')
print()
for i in range(1, 10, 2):
    print(i, end = ' ')


List = ["Noah", "Minsu", "keily", "Yuri"]
for name in List:
    print("%s, Congratulation!" % name)


n = int(input("몇 단? "))
for i in range(1, 10):
    print("%d * %d = %d" % (n, i, n*i))


for i in range(1, 11):
    print(i)


n = int(input())
for i in range(1, n + 1):
    print(i)


for i in range(1, 101):
    if(i % 2 == 0):
        print(i)


n = input()
for i in range(5):
    print(n)


n = int(input())
a = input()
for i in range(n):
    print(a, end = '')


sum = 0
h_list = [159, 163, 173, 158, 169]
for h in h_list:
    sum += h
print("sum : %d" % sum)
print("avg : %.2f" % (sum/len(h_list)))


Sum = 0
num = 0
a = 0
while(1):
    a = int(input())
    if(a == -1):
        print("Sum : %d" %Sum)
        print("avg : %.2f" %(Sum/num))
        break
    Sum += a
    num += 1


for i in range(5, 0, -1):
    for j in range(1, 7 - i):
        print("*", end = '')
    print()
'''

ch = '*'
for i in range(1, 6):
    print(ch * i)
