# if语句
# x = int(input("Please enter an integer:"))

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# for语句
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)

# range 默认的step就是1，可以设置step哦
for i in range(5):
    print(i)

for i in range(0, 10, 2):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# range返回的是一个对象，而不是一个列表， list函数是一个迭代器,创建一个列表从 可迭代的
print(list(range(10)))

# break continue 和 else
# break 跳出循环
# 循环有可能有一个else，当循环中止(for)或者条件(while)是false，但不是通过break中止的循环
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# pass 语句 pass什么都不干，一般用于声明
def initlog(*args):
   pass

# 定义函数
def fib(n):
    """Print a Fibonacci series up to n,"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print(a)

fib(100)

# def关键字用于定义函数，

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n :
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)

# 定义函数，可以设置默认的
def ask_ok(prompt, retries=4, reminder=""):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# ask_ok('whafd', 2, 'com on')

i = 5
def f(arg=i):
    print(arg)

i = 6
f()

# 默认值只计算一次，如果是可变的对象的话，会累计调用
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# 如果不希望在后续调用之间共享默认值，则可以改写该功能
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# 关键字参数(Keyword Arguments)
def parrot(voltage, state='s stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# parrot(1000)
# parrot(voltage=1000)
# parrot(voltage=10000, action='VOOOM')
# parrot(action='VOOm', voltage=10000)
# parrot('a million', 'bereft of life', 'jump')
# parrot('a million', 'bereft of life', 'jump', '打屎你')
# parrot('你不要过来', state='我是你爸爸')

# 非关键字参数，不能写在关键字参数之后
# parrot(voltage=5.0, '你想拿是')

# **name 接收一个字典 *name 接收一个元祖
def cheeseshop(kind, *arguments, **keywords):
    print("你不要过来")
    print('救命啊')
    for args in arguments:
        print(args)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

