# 输入输出

# str() 函数的意思是返回相当于人类可读的值得表示，而repr()则意味着生成表示，可以被解释器读取
# 对于没有特定表示的对象str()和repr()相同的值。字符串有两个不同的表示

s = 'Hello, world'
print(str(s))

print(repr(s))

print(str(1/7))
print(repr(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
hello = 'hello, world\n'
hellos = repr(hello)
print(hello)
print(hellos)

print(repr((x, y, ('天秀'), ('造化钟神秀'))))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end='')
    print(repr(x*x*x).rjust(11))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# str.rjust方法，它通过左边填充空格，在将在左边填充空格

# 左边填充0
print('12'.zfill(5))

print('-003.14'.zfill(7))

# 没有截断
print('3.1415926'.zfill(5))

print('像{}没有明白一样大叫:"{}!"'.format('从来', '不是很开心'))

print('{0} and {1}'.format('真的', '我是'))
print('{1} and {0}'.format('真的', '我是'))

# 关键字参数也可以用于str.format()方法
print('{you} 不入虎穴焉得虎子 {we} 管鲍之交'.format(you='每次看到', we='再也不能直视'))

# 位置和关键字参数可以自由组合
print('{0}要像{1}把夜空飞过 品味泪干的{adjective}'.format('我', '小鸟', adjective='赶脚') )

# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr())
contents = '挣扎'
print('越是{!a}，越是难以逃脱呀'.format(contents))
print('越是{!s}，越是难以逃脱呀'.format(contents))
print('越是{!r}，越是难以逃脱呀'.format(contents))

# :可以控制格式化
import math
print('π的值是多少呀，{0:.10f}'.format(math.pi))

print("But i'll {0:10} only stay with {1:10s} you one more night ".format('口', '我'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
    'Dcab: {0[Dcab]:d}'.format(table))

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

print(vars())