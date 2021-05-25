import random

sum = 0
for x in range(1, 101):
    sum += x
print(sum)

sum = 0 
for x in range(1, 101, 2):
    sum += x
print(sum)

sum = 0 
for x in range(100, 0, -2):
    sum += x
print(sum)


"""
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入: '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('猜对了')
        break
    print('你共猜了了%d次' % counter)
    if counter > 7:
        print('你的智商余额不足')
"""

print(4//2)
# 练习1：输入一个正整数判断是不是素数

from math import sqrt

num = int(input('请输入一个正整数:'))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)

#练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。

x = int(input('x= '))
y = int(input('y= '))
if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d和%d的最大公约数是%d" % (x, y, factor))
        print("%d和%d的最小公倍数是%d" % (x, y, x * y // factor))
        break