import os
import time

#在屏幕上显示跑马灯文字。
def func():
    content = "北京欢迎你为你开天辟地…………"
    while(True):
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

#func()


#设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

import random

def generate_code(code_len=4):
 
    all_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]

    return code

print(generate_code())

#计算指定的年月日是这一年的第几天
def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

test = [
        [1],
        [2],
        [3],
        [4]
    ][False]

print(test)

def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

# 杨辉三角
def Yanghui_triangle():
    num = int(input('Numbers of row: '))
    yh  = [[]] * num
    for row in range(num):
        print('\n')
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t') 
        

Yanghui_triangle()