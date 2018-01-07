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

# old string formatting
print('The value of PI is approximately %5.3f.' % math.pi)

# 读写文件 第一个参数包含文件名，第二个参数是代表模式
# 'r'以只读方式打开文件。文件的指针将会放在文件的开头，如果文件不存在，会发生异常
# 'r+'打开一个文件用于读写。文件指针将会放在文件的开头
# 'w'打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
# 'w+'打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
# 'wb'以二进制写方式打开文件，只用于写文件。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
# 'wb+'以二进制写方式，可以读、写文件。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
# 'rb'以二进制读方式打开文件。只能读文件，文件的指针将会放在文件的开头，这是默认模式，如果文件不存在，会发生异常
# 'rb+'以二进制读方式打开，可以读、写文件，如果文件不存在，会发生异常
# 'a'打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。文件不存在，创建新文件进行写入。
# 'ab'以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。不存在则创建。
# 'a+'打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是
# 'rt' 以文本读方式打开，只能读文件，如果文件不存在会发生异常
# 'wt' 以文本写方式打开，只能写文件，如果文件不存在创建该文件，如果文件存在，先清空，在打开文件
f = open('apply/font/font2.txt', 'r')
f.close()
# 使用with关键字，文件会在合适时间自动关闭

# 文件对象的方法 read方法 读取一些数据
with open('apply/font/font2.txt', 'r') as f:
    # print(f.read(222))
    # print(f.read(12))
    # print(repr(f.readline()))
    for line in f:
        print(line, end='')
    # print(list(f))
    # print(f.readlines())
    print(f.tell())

# write方法
with open('output/writeobject.txt', 'w') as f:
    value = ('the answer', 42)
    s = str(value)
    print(f.write(s))

with open('output/seekwrite.txt', 'wb+') as f1:
    print(f1.write(b'Hello World'))
    print(f1.seek(5))
    print(f1.read(1))
    print(f1.seek(-3, 2)) # seek(offset, from_what) 通过将偏移量添加到参考点来计算；参考点由
    # from_what选择， 0：文件开始 1：当前文件位置 2：文件结尾
    print(f1.read(1))

# 在读写二进制数据的时候，字节字符串和文本字符串的语义差异可能会导致一个潜在的陷阱。
# 索引和迭代动作返回的是字节的值而不是字节字符串
t = 'Hello World'
for c in t:
    print(c)

b = b'Hello World'
for c in b:
    print(c)
# 在文本文件中（在模式字符串中没有b的情况下打开的文件），
# 只允许相对于文件的开头寻找（例外情况是以seek（0，2）寻找文件尾），
# 唯一有效的偏移值是 那些从f.tell（）返回的，或者是零。 任何其他偏移值都会产生未定义的行为。

# 用json保存结构化数据
import json
print(json.dumps([1, 'simple', 'list']))

print(json.dumps("\"foo\bar"))

print(json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'), indent=4))

print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))