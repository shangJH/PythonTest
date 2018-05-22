'''
    chap09 使用Matplotlib绘图
'''
import numpy as np
import matplotlib.pyplot as plt

# 多项式系数
func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
func1 = func.deriv(m=1)        # 一阶导数
x = np.linspace(-10, 10, 30)
y = func(x)
y1 = func1(x)

plt.plot(x, y, 'ro', x, y1, 'g--')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()


# 绘制多项式函数及其导数
func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
x = np.linspace(-10, 10, 30)
y = func(x)
func1 = func.deriv(m=1)
y1 = func1(x)
func2 = func.deriv(m=2)
y2 = func2(x)


plt.subplot(311)
plt.plot(x, y, 'r-')
plt.title("Polynomial")

plt.subplot(312)
plt.plot(x, y1, 'b^')
plt.title("Firsr Derivative")

plt.subplot(313)
plt.plot(x, y2, 'go')
plt.title("Second Derivative")
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 直方图 hist函数

# 对数坐标图



















