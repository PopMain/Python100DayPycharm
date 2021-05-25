value = float(input('input length : '))
unit = input('input unit : ')
if (unit == 'in' or unit  == '英寸'):
    print('%.2ff英寸=%.2f厘米' %(value, value * 2.54))
if (unit == 'cm' or unit=='厘米'):
    print('%.2f厘米=%.2f英寸' %(value, value / 2.54))
else:
    print('请输入有效的单位')


