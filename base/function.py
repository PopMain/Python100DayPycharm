def fac(num):
    result = 1
    for n in range(1, num+1):
        result *= n
    return result
m = int(input('m = '))
n = int(input('n = '))
print(fac(m) // fac(n))

def add(a = 0, b = 0, c= 0):
    return a + b + c
print(add())
print(add(1, 2, 3))
print(add(5, 9))
print(add(a=2, c=5))

def gcd(x, y):
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if (x % factor == 0 and y % factor == 0):
            return factor


import module_goodbye as goodbye
import module_hello as hello

hello.foo()
goodbye.foo()

def foo():
    b = 'hello'
    def bar():
        c = True
        global a
        a = 200
        print(a)
        print(b)
        print(c)
    bar()

if __name__ == '__main__':
    a = 100
    foo()
    print(a)
