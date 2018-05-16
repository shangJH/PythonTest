'''
   chap05 矩阵和通用函数
'''

import sys
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# 创建矩阵, 空格分隔列，分号分隔行
A = np.mat('1 2 3; 4 5 6; 7 8 9')
print(A)     # 矩阵
print(A.T)   # A的转置
print(A.I)   # A的逆

# 使用numpy数组创建矩阵
print(np.mat(np.arange(9).reshape(3, 3)))

# 从已有矩阵创建新矩阵
A = np.eye(2)
print(A)
B = 2 * A
print(B)
print(np.bmat("A B; A B"))   # 注意这种复合矩阵的写法

# 创建通用函数
def ultimate_answer(a):
    result = np.zeros_like(a)
    result.flat = 42
    return result

ufunc = np.frompyfunc(ultimate_answer, 1, 1)
print("The answer:", ufunc(np.arange(4)))
print("The answer:", ufunc(np.arange(4).reshape(2, 2)))

# 通用函数的方法
'''
   通用函数有4个方法，这些方法只对输入两个参数，输出一个参数的ufunc对象有效
'''
a = np.arange(9)
print(np.add.reduce(a))
print(np.add.accumulate(a))
print(np.add.reduceat(a, [0, 5, 2, 7]))  # 这个过程较绕，结果等价如下：
print(np.add.reduce(a[0:5]))
print(a[5])     # 因为5 > 2, 所以只取a[5]
print(np.add.reduce(a[2:7]))
print(np.add.reduce(a[7:]))

# 数组的除法运算 divide函数  true_divide函数  floor_divide函数
a = np.array([2, 6, 5])
b = np.array([1, 2, 3])
print("Divide", np.divide(a, b), np.divide(b, a))
print("Divide", np.true_divide(a, b), np.true_divide(b, a))
print("Divide", np.floor_divide(a, b), np.floor_divide(b, a))   # 向下取整

print(a/b, b/a)    # 等价于divide
print(a//b, b//a)  # 等价于floor_divide

# 模运算 计算模数或者余数，可以使用numpy中的mod, remainder和fmod函数，当然也可以使用%运算符，区别主要在于处理负数的方式
a = np.arange(-4, 4)
print(np.remainder(a, 2))
print(np.mod(a, 2))
print(a % 2)
print(np.fmod(a, 2))   # 只有这个与上面的结果不同，存在负数的结果

# rint函数对浮点数取整但不改变浮点数类型
F = np.matrix([[1,1],[1,0]])
print(F)
print((F ** 7)[0, 0])

n = np.arange(1, 9)


# 利萨茹曲线
a = 9
b = 8
t = np.linspace(-np.pi, np.pi, 201)   # 区间[-pi, pi]分成201等份
x = np.sin(a * t + np.pi / 2)
y = np.sin(b * t)
plot(x, y)
show()

# 方波   使用方波的傅里叶级数生成方波
t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, 200)
k = 2 * k - 1
f = np.zeros_like(t)
for i in range(len(t)):
    f[i] = np.sum(np.sin(k * t[i]) / k)
f = (4 / np.pi) * f
plot(t, f)
show()


# 绘制锯齿波和三角波
t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, 1000)
f = np.zeros_like(t)

for i in range(len(t)):
    f[i] = np.sum(np.sin(2 * np.pi * k * t[i]) / k)
# 摆脱上述的循环函数，可以大大提高程序效率
f = (-2 / np.pi) * f
print(f, len(f))
plot(t, f, lw=1.0)
plot(t, np.abs(f), lw=2.0)
show()

a = np.arange(3)
b = np.arange(3)
print(a, b)
print(a * b)


# 位操作符合比较函数
# XOR 或者 ^
x = np.arange(-9, 9)
y = -x
print((x ^ y) < 0)
print(np.less(np.bitwise_xor(x, y), 0))           # 判断符号
print((x & (x - 1)) == 0)
print(np.equal(np.bitwise_and(x, (x - 1)), 0))    # 检查是否为2的幂
print(x & ((1 << 2) - 1))
print(np.bitwise_and(x, np.left_shift(1, 2) - 1))












