'''
   chap06 深入学习NumPy模块
'''

import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# numpy.linalg模块包含线性代数的函数。使用这个模块可以计算逆矩阵、求特征值、解线性方程组以及求解行列式
A = np.mat("0 1 2; 1 0 3; 4 -3 8")
print(A)

inverse = np.linalg.inv(A)
print("inverse of A ", inverse)
print("check", A * inverse)

# 求解线性方程组
A = np.mat("1 -2 1; 0 2 -8;-4 5 9")
b = np.array([0, 8, -9])
x = np.linalg.solve(A, b)
print("Solution", x)
print("Check", np.dot(A, x))

# 求特征值和特征向量
A = np.mat("3 -2;1 0")
print("Eigenvalues", np.linalg.eigvals(A))

eigenvalues, eigenvectors = np.linalg.eig(A)
print("First tuple of eig", eigenvalues)
print("Second tuple of eig", eigenvectors)
for i in range(len(eigenvalues)):
    print("Left", np.dot(A, eigenvectors[:,i]))
    print("Right", eigenvalues[i] * eigenvectors[:,i])

# 奇异值分解
A = np.mat("4 11 14;8 7 -2")
print(A)
U, sigma, V = np.linalg.svd(A, full_matrices=False)
print("U", U)
print("Sigma", sigma)
print("V", V)
print("Check", U * np.diag(sigma) * V)

# 广义逆矩阵
A = np.mat("4 11 14;8 7 -2")
print(A)
pseudoinv = np.linalg.pinv(A)
print("Pseudo inverse", pseudoinv)
print("Check", A * pseudoinv)

# 计算行列式
A = np.mat("3 4;5 6")
print("Determinant", np.linalg.det(A))

# 快速傅里叶变换
x = np.linspace(0, 2 * np.pi, 30)
wave = np.cos(x)
transformed = np.fft.fft(wave)
print(np.all(np.abs(np.fft.ifft(transformed) - wave < 10 ** -9)))
plot(transformed)
# show()

# 移频
shifted = np.fft.fftshift(transformed)
print(np.all(np.abs(np.fft.ifftshift(shifted) - transformed < 10 ** -9)))
plot(transformed, lw=2)
plot(shifted, lw=3)
# show()

# 随机数
cash = np.zeros(10000)
cash[0] = 1000
outcome = np.random.binomial(9, 0.5, size=len(cash))
for i in range(1, len(cash)):
    if outcome[i] < 5:
        cash[i] = cash[i - 1] - 1
    elif outcome[i] < 10:
         cash[i] = cash[i - 1] + 1
    else:
        raise AssertionError("Unexpected outcome" + outcome)

print(outcome.min(), outcome.max())
plot(np.arange(len(cash)), cash)
# show()

# 超几何分布

# 连续分布

# 绘制正态分布

# 对数正态分布

