'''
    chap01
'''
import numpy as np
import datetime

# numpy用法1 - 向量加法
def numpysum(n):
    a = np.arange(n) ** 2   # numpy的arange()函数创建0~n的整数向量
    b = np.arange(n) ** 3
    c = a + b
    return c




