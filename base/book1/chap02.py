'''
   chap02   非常少的内容
'''

# python3中所有字符串已经使用unicode编码

# 如果模块、类或者函数定义的第一条语句是一个字符串，该字符串就成为了相关对象的文档字符串
def fact(n):
    "This function computes a factorial"
    if(n <= 1): return 1
    else: return n * fact(n - 1)

print(fact.__doc__)

# 装饰器，函数、方法或类定义的前面可以使用一个特殊的符号，成为装饰器，其目的是修改后面定义的行为
class Foo(object):
    @staticmethod
    def bar():
        pass

# 可以使用多个装饰器，但每个装饰器必须各占一行