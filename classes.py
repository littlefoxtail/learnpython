# 类提供了将数据和功能捆绑在一起的方法
# 范围和命名空间

# local分配不会改变 scope_test绑定的spam
# nonlocal会改变 scope_test绑定
# global分配会改变模块级别的绑定

def scope_test():
    def do_local():
        spam = 'local spam'
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
scope_test()
print("In global scope", spam)

# 初告白
# class ClassName:
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
print(MyClass.i)
print(MyClass.f)
print(MyClass.__doc__)

# 类实例使用函数表示法
x = MyClass()

# 当定义一个__init__()方法，类初始化会自动调用__init__()创建类
# __init__()可以有参数

# Create a class with a variable inside and an instance of that class
class One:
    color = 'green'

obj2 = One()


# Here we create a global variable(outside a class suite).
color = 'blue'         

# Create a second class and a local variable inside this class.       
class Two:             
    color = "red"

    # Define 3 methods. The only difference between them is the "color" part.
    def out(self):     
        print(self.color + '!')

    def out2(self):
        print(color + '!')

    def out3(self):
        print(obj2.color + '!')

# Create an object of the class One
obj = Two()

obj.out()
obj.out2()
obj.out3()


# Objects初始化
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

# 另一种属性引用是方法
# function是按名称调用的一段代码。它可以传递数据操作，并可以选择返回数据。所有传递给函数的数据都被显示传递
# method是由与对象关联的名称调用的一段代码。在大多数方面，除了两个，与function相同
# 1. method隐式地传递了被调用对象
# 2. method能够对类中包含的数据进行操作

print(x.f())

xf = x.f
print(xf())


# 实例变量是针对每个实例唯一的数据，而类变量则是针对类的所有实例共享的属性和方法
class Dog:
    
    kind = 'canine'

    def __init__(self, name):
        self.name = name

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

# 共享数据可能会涉及可变对象，会出现一个搞笑的效果
# 以下代码中的tricks不应该用作类变量，因为只有一个列表将被所有的Dog2实例共享


class Dog2:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d1 = Dog2('Fido')
e1 = Dog2('Buddy')
d1.add_trick('roll over')
e1.add_trick('play dead')
print(d1.tricks)

# 正确的作法是用作一个实例变量
class Dog3:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

    def add_other_trick(self):
        print('fdaf')
    
d3 = Dog3('Fido')
e3 = Dog3('Buddy')
d3.add_trick('roll over')
e3.add_trick('play dead')
print(d3.tricks)
print(e3.tricks)

d3.add_other_trick()

# self代表类的示例，而非类 实际上 python解释为Dog3.add_trick(d3, 'roll over')
# self在定义时需要定义，但是在调用时会自动传入。
# self的名字并不是规定死的，但是最好还是按照约定是用self
# self总是指调用时的类的实例。

# self可以不写吗？如果是对象调用，self在定义时候不可以省略
# 但是如果定义和调用均不传类实例是可以的，这就是类方法

def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1
    
    def g(self):
        return 'hello world'

    h = g

# f g 和h 都是类C的所有属性，他们都是指向函数对象的，
c = C()
print(c.h())

# 继承
# 派生类的定义
# class DerivedClassName(BaseClassName):
#     <statement-1>
#     .
#     .
#     .
#     .
#     <statement-N>

# 派生类中的重要的方法事实上可能需要扩展而不是简单的替换同名的基类方法。

# 继承 内建函数
# isinstance()去检查实例的类型
# issubclass()去检查类的继承关系， issubclass(bool, int) 如果bool 是int的子类则返回true

# 多继承
# python支持多继承(嘿嘿，java君 怕不怕!) 多继承的定义
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     .
#     <statement-N>

# Python不存在私有实例变量，但是大多数python代码都有一个约定：以下划线作为前缀的名称应被视为API的非公开部分


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        print('Mapping')
        for item in iterable:
            self.items_list.append(item)
    
    __update = update
    print(__update)

class MappingSubclass(Mapping):
    def update(self, keys, values):
        print('MappingSubclass')
        for item in zip(keys, values):
            self.items_list.append(item)

# zip是python中的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个
# tuple(元祖)，然后返回由这些tuple组成的list。
ms = MappingSubclass([1, 2, 3])
ms.update([1, 2], [23, 2])
print(ms.items_list)


om = Mapping([1, 2, 4, 6])
om.update([323, 534])
print(om.items_list)


class Employee:
    def eoe(self):
        print('hell')

    m = eoe


john = Employee()

john.name = "王晓晓"
john.dept = 'computer lab'
john.salary = 1000

# 方法对象也拥有属性

print(john.eoe)

print(john.m.__self__)
print(john.m.__func__)




    
# Iterators

# for循环这种访问方式清晰，间接，方便。迭代器的使用遍历。在幕后
# for语句在容器对象上调用iter()。该函数返回一个迭代器对象，该对象定义了一次访问容器中元素的
# 方法__next__()。当没有更多的元素，__next__()引发一个StopIteration异常，
for element in [1, 2, 3]:
    print(element) 

a = 'abc'
it = iter(a)
print(it)

print(next(it))
print(next(it))
# print(next(it))
# print(next(it))

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
iter(rev)

for char in rev:
    print(char)

# Generators
# 生成器是创建迭代器的简单而强大的工具。它们像常规函数一样编写，但是只要他们想返回数据就使用yield语句
# 每当next()被调用时，生成器会从停止的地方恢复（记忆所有的数据值以及上次执行的语句）
print('------Generators-----')

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('golf'):
    print(char)

# 任何可以用发生器完成的事情也可以使用前面部分描述的基于类的迭代器来完成。什么使得生成器如此紧凑

# Generator Expressions
# 生成器表达式

# 简单的生成器可以使用类似于列表解析的语法简洁地编码为表达式，但是括号而不是方括号。这些表达式适用于通过封闭函数立即使用生成器的情况。
# 生成器表达式比完整的生成器定义更紧凑但功能更少，往往比等效的列表解析更具有内存友好性

print(sum(i*i for i in range(10)))
lo = []
for i in range(10):
    lo.append(i*i)
print(sum(lo))

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))

from math import pi, sin
sine_table = {x: sin(x*pi/180) for x in range(0, 91)}
unique_words = set(word for line in page for word in line.split())


