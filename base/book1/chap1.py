'''
    <<python编程手册-第4版>> 第一章代码
'''

# print函数
import sys

print("Hello, world")

# 2.x版本计算会有问题，3.x之后版本计算正常
print(6000 + 4532.50 + 132.12)

# 程序可以通过抛出该异常退出
# raise SystemExit

# 简单的复利计算
principal = 1000
rate = 0.05
numberyears = 5
year = 1
while year < numberyears:
    principal = principal * (1 + rate);   # python3计算保留精度比python2高了许多
    print(year, principal)
    print("%3d %.2f" % (year, principal))                 # 使用元组的方式传递参数
    print(format(year, "3d"), format(principal, ".2f"))   # 使用format单个格式化每个待打印的参数
    print("{0:3d} {1:.2f}".format(year, principal))      # 另外一种写法
    year += 1

# 条件语句 python中没有专门的switch或case语句用于检测多个值，要检验多个条件，可以使用elif语句; pass表示什么也不做
'''
   if a < b:
      xxx
   else
      pass

   if语句可以和and, or, not关键字组成布尔表达式
'''

#  python中的布尔值为True何False, in用于检查某个值是否包含在另一个对象
s = "test in spam string"
has_spam = not 'spam' in s       # 前面可以加not，取反
print(has_spam)


# 文件的输入和输出，默认设置为gbk，但是文件是utf-8格式，所以需要加上encoding参数
f = open("../../resources/doc/test1.txt", encoding = 'utf-8')
line = f.readline()   # 读取一行
while line:
    print(line, end='')
    line = f.readline()   # 读取下一行

print("\n-------------------------------------------------------------------------------------\n")

# 一种简洁的读取文件内容写法
for line in open("../../resources/doc/test1.txt", encoding="utf-8"):
    print(line, end='')  # print会有一个换行，原先文件每行也有一个换行符，如果不加上每行会多出一个空白行


# 将前述计算结果写入文件
f = open("../../resources/doc/out.txt", "w", encoding = 'utf-8');
year = 1
principal = 1000
while year < numberyears:
    principal = principal * (1 + rate);   # python3计算保留精度比python2高了许多
    print("%3d %.2f" % (year, principal), file=f)   # 这里不用加上\n，print函数会自动添加
    # f.write("%3d %.2f\n" % (year, principal))
    year += 1

print("\n---------------------------------------------------------------------------\n")

# python3中的输入
# print("Enter your name:")   # 如果换成书中的sys.stdout.write("Enter your name:") 则会存在一些顺序问题，如果在print函数中添加参数end=''，同样会出现顺序问题
# name = sys.stdin.readline()   # 读取输入的一行
# print("input name : %s" % name, end='')

# input()函数
# name = input("Enter your English name:")    # 光标位置会有点问题
# print("English name: %s" % name)


# 字符串
'''
  创建字符串字面量，可以使用单引号，双引号和三引号，三引号可以跨行
  切片规则，和matlab中的类似
'''
a = "Hello World"
print("a[4] = %s" % a[4])
print("a[:5] = %s" % a[:5])
print("a[6:] = %s" % a[6:])
print("a[3:8] = %s" % a[3:8])

# +号在python中同样可以连接两个字符串
g = a + " This is a test"
print("test +: %s" % g)

# int() float() / str()  repr()  format
x = "37"
y = "45"
print("%s + %s =  %s" % (x, y, x + y) )
print("int(%s) + int(%s) =  %s" % (x, y, int(x) + int(y)))   # int()函数将字符串转换成整型，类似的还有float()函数

x = 3.4
print("str(%s) = %s" % (x, str(x)))
print("repr(%s) = %s" % (x, repr(x)))
print("format(%s) = %s" % (x, format(x, "0.5f")))  # format()函数具有格式化功能


# 列表










