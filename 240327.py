'''
list1 = []
list2 = [1, 2, 3]무조건 문자열
list3 = ['a', 'b', 'c']
list4 = ["hello", 'world']
list5 = [1, 2, 'a', 'b', 'python']
list6 = [1, 2, ['a', 'b', 'c'], 3]

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)


a = "Python"
b = " is fun"
print(a + b)
print(a * 2)


a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a * 3)


a = '*'
print(a * 10)


a = [1, 2, 3, 4, 5, 6]
print(a[-1])


a = [10, 20, [30, 40], 50]
print(a[2])
print(a[2][0])
print(a[2][1])


a = "Carpe Diem!"
print(a[6:11])

a = "Carpe Diem!"
print(a[6:])

b = [1, 2, 3, 4, 5, 6]
print(b[:3])


a = "Carpe Diem!"
print(a[-5:-1])
a = "Carpe Diem!"
print(a[:-6])


a = [10, 20, 30, 40, 50]
print(a[0])
a = [10, 20, [30, 40], 50]
print(a[2])
print(a[2][0])
print(a[2][1])


a = [10, 20, 30, 40, 50]
a[0] = 'a'
print(a)
a[1:3] = 'b'
print(a)


list1 = 'I Love You'
print(list1.count('o'))

print(list1.find('Y'))

print(list1.index('Y'))#첫번째 거만

print('.'.join(list1))

print(list1.split())

print(list1.replace('Love', 'like'))

print(list1.upper())

print(list1.lower())


a = '       abcd              '
b = 'efgh'
print('%s%s' %(a, b))
a = a.strip()
print('%s%s' %(a, b))


list1 = 'Hello World'
list2 = 'python'
list3 = 'oh!my!god'

print(list1.count('l'))
print(list2.find('p'))
print(list3.split('!'))


a = [1, 5, 10, 3]
a.append(20)
print(a)
a.sort()
print(a)
a = ['b', 'a', 'n', 'a', 'n', 'a']
a.reverse()
print(a)
a.remove('a')
print(a)
p = a.pop()
print(p, a)
n = a.count('n')
print(n)


num = input('생년 월일 : ')

a = num[:2] + '-' + num[3:5] + '-' + num[6:]
b = '20' + num[:2]

print('생년월일 : ',a)
print('출생년도 : ',b,'년')
print('태어난달 : ',num[3:5])
print('태어난일 : ',num[6:])
'''

num = input('생년 월일 : ')

a = num[:2] + num[2:]
print('생일 : ', a)
