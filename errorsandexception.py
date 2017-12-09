# while True:
#     try:
#         x = int(input('Please enter a number:'))
#         break
#     except ValueError:
#         print("Oops! That was no valid number. Try again...")


# import sys
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:{0}".format(err))
# except ValueError:
#     print('Could not convert data to an integer.')
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

# try ... except语句有一个可选的else子句，如果有，必须在所有except之后，如果没有捕获异常，这段代码必须被执行
# else子句的使用要比向try子句中添加额外的代码要好，因为它避免了意外捕获由try...except语句保护的代码没有引发的异常
try:
    print('try----')
    raise ValueError('error')
except ValueError:
    print('value Error')
else:
    print('else')

# 发生异常时，可能有一个关联的值，也就是异常的参数。参数的存在和类型取决于异常类型。

# except子句可以在异常名称之后指定一个变量。该变量绑定到一个异常实例，存储在instance.args中
# 为了方便起见，异常实例定义了__str__()，所以参数可以直接打印，而不必引用args。也可以在引发异常之前初始化异常，并根据需要添加任何属性
try:

    e = Exception('spam', 'eggs')
    e.like = 'like'
    raise e
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x = ', x)
    print('y = ', y)
    print(inst.like)

# Raising Exceptions
# raise语句允许程序员强制执行指定的异常
# raise NameError('HiThere')

# 传递一个异常类，将调用无参构造
# raise ValueError

# 如果你打算确定是否引发异常，不打算处理，可以用更简单的raise
try:
    raise NameError('我爱天安门')
except NameError:
    print("an exception")
    # raise

# 自定义Exception
class Error(Exception):
    """
    Base class for exceptions in this module
    """
    pass

class InputError(Error):
    """
    Attributes:
        expression
        message
    """
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

# try语句有另一个可选的子句，用来定义在任何情况下都必须执行的清理操作
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# 预定义的清理操作
# 一些对象不再需要了要执行标准的清理操作
# with语句允许像文件这样的对象以确保它们总是被及时清理的方式来使用