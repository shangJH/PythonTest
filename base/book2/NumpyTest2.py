'''
   chap03 常用函数
'''
import sys
import datetime
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show


i2 = np.eye(2)
print(i2)
np.savetxt("../../resources/doc/eye.txt", i2)

# 获取收盘价与成交量数据
c,v = np.loadtxt('../../resources/csv/data.csv', delimiter=',', usecols=(6,7), unpack=True)
print(c, v)
vwap = np.average(c, weights=v)
print("VWAP = %s" % vwap)

print(np.mean(c))

# max、min和ptp函数
print(np.max(c))
print(np.min(v))
print(np.ptp(c))        # 计算最大值和最小值的差值

print(np.median(c))     # 计算c向量的中位数，如果向量元素为偶数，中位数 = (sorted_c[N / 2] + sorted_c[M / 2 + 1]) / 2
print(np.msort(c))      # 排序函数
print(np.var(c) == np.mean((c - c.mean()) ** 2))   # 方差 = 各数据与所有数据算术平均数的差的平方和除以数据个数

returns = np.diff(c) / c[: - 1]  # diff函数可以返回一个由相邻数组元素的差值构成的数组，返回的数组相比原数组少一个元素
print(returns)

# std函数计算标准差


# 将日期字符串转换成数字，星期一:0，剩下以此类推
def datestr2num(s):
    # s这里可能是bytes类型，需要转成字符串形式
    return datetime.datetime.strptime(s.decode(), "%d-%m-%Y").date().weekday()

dates, close = np.loadtxt('../../resources/csv/data.csv', delimiter=',', usecols=(1, 6), converters={1:datestr2num}, unpack=True)
print("Date = ", dates)

# zeros函数
averages = np.zeros(5)    # 生成包含7个元素的数组
print(averages)
# where函数会根据指定的条件返回所有满足条件的数组元素的索引值, take函数可以按照这些索引值从数组中取出相应的元素
for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close, indices)
    print(prices)
    avg = np.mean(prices)
    averages[i] = avg

print(averages)
print(np.argmax(averages))  # argmax返回的是最大元素的索引值
print(np.argmin(averages))  # argmin返回的是最小元素的索引值


# 周汇总
# apply_along_axis函数，这个函数会调用另一个由我们给出的函数，作用与每一个数组元素上
dates, open, high, low, close = np.loadtxt('../../resources/csv/data.csv', delimiter=',', usecols=(1, 3, 4, 5, 6), converters={1:datestr2num}, unpack=True)
close = close[:16]
dates = dates[:16]   # 取前3周数据

first_monday = np.ravel(np.where(dates == 0))[0]
print("The first monday index is %s" % first_monday)
last_monday = np.ravel(np.where(dates == 4))[-1]
print("The last monday index is %s" % last_monday)

week_indices = np.array(np.arange(first_monday, last_monday + 1))
week_indices = np.split(week_indices, 3)  # 分成3份
print(week_indices)

def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]
    return("APPL", monday_open, week_high, week_low, friday_close)

weeksummary = np.apply_along_axis(summarize, 1, week_indices, open, high, low, close)
print(weeksummary)
np.savetxt('../../resources/csv/weeksummary.csv', weeksummary, delimiter=',', fmt="%s")

# 真实波动幅度均值
h, l, c = np.loadtxt('../../resources/csv/data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)
N = 10
h = h[-N:]   # 取最后10天交易数据
l = l[-N:]
previousclose = c[-N -1:-1]   # 相对应上面的交易日数据的前一天交易数据
truerange = np.maximum(h - l, h - previousclose, previousclose - l)
print("True range ", truerange)

atr = np.zeros(N)
atr[0] = np.mean(truerange)   # 计算平均波动情况
for i in range(1, N):
    atr[i] = (N - 1) * atr[i - 1] + truerange[i]
    atr[i] /= N
print("ATR ", atr)


# 简单移动平均线   convolve函数
N = 5
weights = np.ones(N) / N
sma = np.convolve(weights, c)[N-1:-N+1]
t = np.arange(N - 1, len(c))
# plot(t, c[N - 1:], lw=1.0)
# plot(t, sma, lw=2.0)
# show()

# 指数移动平均线
x = np.arange(5)
print("Exp ", np.exp(x))
print("Linspace", np.linspace(-1, 0, 5))  # -1到0之间，分成5等份

weights /= weights.sum()
print("Weights", weights)
ema = np.convolve(weights, c)[N-1:-N+1]
t = np.arange(N - 1, len(c))
# plot(t, c[N-1:], lw=1.0)
# plot(t, ema, lw=2.0)
# show()


# 布林带

# 线性模型
N = 10
b = c[-N:]
b = b[::-1]   # 反序
print("b", b)

A = np.zeros((N, N), float)
# print("Zeros N by N", A)
for i in range(N):
    A[i, ] = c[-N - 1 - i: -1 - i]

(x, residuals, rank, s) = np.linalg.lstsq(A, b)   # 线性估计模型
print(x, residuals, rank, s)

print(np.dot(b, x))














