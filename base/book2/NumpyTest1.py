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


# 创建多维数组
m = np.array([range(2), range(2)])    # range() 创建[0 1] 向量
print(m, m.shape)

m = np.array([[1, 2], [3, 4]])
print(m, m[0, 0], m[0][1], m[1][0], m[1][1])

# numpy数据类型
'''
    bool
    inti
    int8
    int16
    int32
    int64
    uint8
    uint16
    uint32
    uint64
    float16
    float32
    float64/float
    complex64
    complex128/complex
'''
a = np.float64(12)
print(np.float64(43), np.int8(12.0), np.float(False), np.float(True), np.bool(43.0))
print(a.dtype.itemsize)  # 占8个字节，打印字节大小

print(np.array(range(7), dtype='f'))   # 生成向量，类型为float32, 占4字节
print(np.array(range(7), dtype='D'))

print(np.dtype(float))   # float64
print(np.dtype('f'))     # float32
print(np.dtype('d'))     # float64
print(np.dtype('f8'))    # float64

# 打印完整NumPy数据类型列表
print(np.sctypeDict.keys())

# dtype类的属性
t = np.dtype('Float64')
print(t.char)    # 获取对应数据类型的字符编码，d -- > Float64










