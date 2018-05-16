'''
   chap04 便捷函数
'''
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# 股票相关性分析
bhp = np.loadtxt('../../resources/csv/BHP.csv', delimiter=',', usecols=(6,), unpack=True)
bhp_returns = np.diff(bhp) / bhp[:-1]
vale = np.loadtxt('../../resources/csv/VALE.csv', delimiter=',', usecols=(6,), unpack=True)
vale_returns = np.diff(vale) / vale[:-1]
# 上述计算收益率 =  股票涨跌幅度 / 本身估价

covariance = np.cov(bhp_returns, vale_returns)    # 计算股票收益率的协方差矩阵
print("Covariance", covariance)

print("Covariance diagonal", covariance.diagonal())   # 对角元素
print("Covariance trace", covariance.trace())         # 计算矩阵的迹，即对角元素之和

print(covariance/ (bhp_returns.std() * vale_returns.std()))
print("Correlation coefficient", np.corrcoef(bhp_returns, vale_returns))

difference = bhp - vale
avg = np.mean(difference)
dev = np.std(difference)

print("Out of sync", np.abs(difference[-1] - avg) > 2 * dev)

t = np.arange(len(bhp_returns))
plot(t, bhp_returns, lw=1)
plot(t, vale_returns, lw=2)
show()

t = np.arange(len(bhp))
poly = np.polyfit(t, bhp - vale, 3)
print("Polynomial fit", poly)

print("Next value", np.polyval(poly, t[-1] + 1))

print("Roots", np.roots(poly))

der = np.polyder(poly)
print("Derivative", der)

print("Extremas", np.roots(der))
vals = np.polyval(poly, t)
print(np.argmax(vals))
print(np.argmin(vals))

plot(t, bhp - vale)
plot(t, vals)
show()





