'''
  chap07 专用函数
'''
import datetime
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import imshow, show

# 排序函数
'''
    sort返回排序后的数组
    lexsort函数根据键值的字典序进行排序
    argsort函数返回输入数组排序后的下标
    ndarray类的sort方法可以对数组进行原地排序
    sort_complex函数对复数按照先实部后虚部的顺序进行排序
'''
def datestr2num(s):
   return datetime.datetime.strptime(s.decode(), "%d-%m-%Y").toordinal()

dates, closes = np.loadtxt('../../resources/csv/AAPL.csv', delimiter=',', usecols=(1, 6), converters={1:datestr2num}, unpack=True)
indices = np.lexsort((dates, closes))
print("Induces", indices)
print(["%s %s" % (datetime.date.fromordinal(int(dates[i])), closes[i]) for i in indices])


# 复数
np.random.seed(42)    # 设置随机种子
# 后面的5表示产生5个随机数组成的数组
complex_numbers = np.random.random(5) + 1j * np.random.random(5)
print("Complex numbers", complex_numbers)
print("Sorted", np.sort_complex(complex_numbers))  # 按照先实部，后虚部的排序方式

# 数组搜索
a = np.array([2, 4, 8])
print(np.argmax(a))        # argmax函数返回数组中最大值对应的下标

a = np.array([2, np.nan, 4])
print(np.argmax(a))        # 如果有nan值就会出错
print(np.nanargmax(a))     # 使用下面的方式就可以忽略nan问题

a = np.array([2, 4, 8])
print(np.argwhere(a <= 4))

# searchsorted函数为指定的插入值返回一个在有序数组中的索引位置，从这个位置插入可以保持数组的有序性
a = np.arange(5)
indices = np.searchsorted(a, [-2, 7])
print("Indices", indices)
# 插入数据并打印结果
print(np.insert(a, indices, [-2, 7]))

# 数组元素抽取
a = np.arange(7)
condition = (a % 2) == 0
# 抽取偶数
print("Even numbers", np.extract(condition, a))
# 抽取非零元素
print("Non zero", np.nonzero(a))

# 金融函数

# 计算分期付款
# 例如贷款100万，年利率为10%，需要30年还清，计算每月还款数额
print("Payment", np.pmt(0.10 / 12, 12 * 30, 1000000))
# 贷款9000，年利率为10%，每月固定还款100的情况下，计算所需的付款期数
print("Number of payment", np.nper(0.10 / 12, -100, 9000))
# 计算利率
print("Interest rate", 12 * np.rate(167, -100, 9000, 0))

# 绘制巴特利特窗
window = np.bartlett(42)
plot(window)
# show()

# 布莱克曼窗平滑股价数据

# 绘制汉明窗
window = np.hamming(42)
plot(window)
# show()

# 绘制凯泽窗
window = np.kaiser(42, 14)
plot(window)
# show()

# 贝塞尔曲线
x = np.linspace(0, 4, 100)
vals = np.i0(x)
plot(x, vals)
# show()

# sinc函数
x = np.linspace(0, 4, 100)
xx = np.outer(x, x)
vals = np.sinc(xx)

imshow(vals)
# show()
