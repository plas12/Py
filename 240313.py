'''
a = 1
print(a)

a = 2
print(a)


a = 123
b = "Hello World"
c = True

print(a, type(a))
print(b, type(b))
print(c, type(c))

a=7
print("%d은 정수이다." % a)
print("원주율은 %lf이다." % 3.14)
print("나의 이름은 %s 이다." % "홍길동")
print("'%c' 등급입니다." % 'A')
print("성공률 : 90%")


print("%15s" % "1hello", end=' ')

print("%-3s" % "2world", end = ' ')
print("%-10s" % "3hello world", end = ' ')


print("내 이름은 {0}이고, {1}년 {2}월 {3}일 에 태어났다.".format("강민", 2012, 4, 7))


print(10/3)
#?
print("%d %d %d" % (5, 3, 6))


name = input("이름 : ")
print("== 자기소개하기 ==")
print("이름 : %s" % name)


a = int(input())
b = int(input())
print(a + b)


a = int(input("a 정수입력 : "))
b = int(input("b 정수입력 : "))
c = int(input("c 정수입력 : "))
print("세 정수의 평균은 %0.2f입니다" % ((a + b + c) / 3))


print("%10s" % "cat", end = ' ')
print("%10s" % "3", end = ' ')
print("%10s" % "3.14")

print("%10s" % "dog", end = ' ')
print("%10s" % "127", end = ' ')
print("%10s" % "1.234")

print("%10s" % "turtle", end = ' ')
print("%10s" % "54321", end = ' ')
print("%10s" % "10.1")


print("%10s%10d%10.2lf"%("Cat", 3, 3.14))

print("%10s%10d%10.3lf"%("Dog", 127, 1.234))

print("%10s%10d%10.1lf"%("Turtle", 54321, 10.1))


L = int(input("L 판매개수 : "))
M = int(input("M 판매개수 : "))
S = int(input("S 판매개수 : "))
sum = 2500 * L
sum = sum + 1000 * M
sum = sum + 500 * S
print("오늘의 총 매출은 %d원 입니다." % sum)


n = int(input("높이 : "))
m = int(input("밑변 : "))
a = n * m / 2
print("넓이 : %.2lf" % a)


i = int(input("inch : "))
a = 2.54 * i
print("%.2lfcm" % a)
'''

a = int(input("a : "))
b = int(input("b : "))
print("%d" % a**b)
