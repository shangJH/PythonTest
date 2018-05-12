'''
   chap03 类型与对象
'''

# is运算符用于比较两个对象，内置函数type则返回一个对象的类型

# def compare(a, b):
#     if a is b:
#         # a和b是同一个对象
#         statements
#     if a == b:
#         # a和b具有相同的值
#         statements
#     if type(a) is type(b):
#         # a和b具有相同类型
#         statements
import copy
import sys

s = []
if type(s) is list:
    s.append("list")

if type(s) is dict:
    s.append("dict")

# isinstance()函数能辨别继承，它是检查所有python对象类型的首选方式
if isinstance(s, list):
    s.append("list")

if isinstance(s, dict):
    s.append("dict")

# 引用计数和垃圾回收
x = 37   # 创建一个值为37的对象
b = x    # 增加37的引用计数
c = []
c.append(b)

print("x的引用计数:", sys.getrefcount(x))   # 引用计数为7？引用计数比你猜测的要大得多。对于不可变数据，解释器会主动在程序的不同部分共享对象，以便节约内存

# del x      # 减少37的引用计数，这个使用之后，后面的x变量就无法使用了
b = 42       # 减少37的引用计数
c[0] = 2.0   # 减少37的引用计数

print("x的引用计数:", sys.getrefcount(x))

# 当一个对象的引用计数归零时，它将被垃圾回收机制处理掉。解释器在执行过程中会定期执行一个周期检测器，搜索不可访问的对象周期并删除他们

# 引用和复制
a = [1, 2, 3, 4]
b = a
print(b is a)   # True
b[2] = -100     # 创建的是引用
print(a)        # [1, 2, -100, 4]

# 浅拷贝和深拷贝
a = [1, 2, [3, 4]]
b = list(a)     # 创建一个a的浅拷贝
print(b is a)
b.append(100)
print(a)        # [1, 2, [3, 4]]
print(b)        # [1, 2, [3, 4], 100]

# 注意下面的
b[2][0] = -100
print(a)        # [1, 2, [-100, 4]]   a和b是单独的列表对象，但是他们包含的元素是共享的

# 深复制将创建一个新对象，并递归复制它包含的所有对象，使用copy.deepcopy()函数完成该工作
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
b[2][0] = -100
print(a)        # [1, 2, [3, 4]]  a中的元素不会变化

#第一类对象
line = "GOOG, 100, 490.10"
field_types = [str, int, float]
raw_fields = line.split(',')
# 注意zip函数的使用
fields = [ty(val) for ty, val in zip(field_types, raw_fields)]
print(fields)

# 数据的内置类型








