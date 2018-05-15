'''
    chap02 Numpy基础
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
print(t.char, t.str)    # 获取对应数据类型的字符编码，d -- > Float64      <f8  大段序是将最高位字节存储在最低的内存地址处，用>标识；小端序将最低字节存储在最低的内存地址处，用<表示

# 创建自定义数据类型
t = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price', np.float32)])
print(t)
print(t['name'])

itemz = np.array([('Meaning of file DVD', 42, 3.14), ('Butter', 12, 2.72)], dtype=t)   # 使用自定义类型
print(itemz[1])

a = np.array(range(9))
print(a[3:7])
print(a[:7:2])
print(a[::-1])   # 已-1步长遍历列表

# 多维数组的切片和索引
b = np.array(range(24)).reshape(2, 3, 4)
print(b.shape)
print(b)

print(b[0,0,0])
print(b[:,0,0])
print(b[0])
print(b[0,:,:])

print(b[0,1])
print(b[0,1,::2])
print(b[...,1])
print(b[:,1])
print(b[0,:,1])
print(b[0,:,-1])
print(b[0,::-1,-1])
print(b[0,::2,-1])
print(b[::1])

# 改变数组的维度
print(b.ravel())       # 展平操作
b.shape = (6,4)        # 改变shape  使用reshape()函数，或者直接给shape赋值
print(b)

print(b.transpose())   # 转置
b.resize((2,12))
print(b)

############## 数组的组合 ####################################
a = np.arange(9).reshape(3,3)
print(a)
b = 2 * a
print(b)

# 水平组合
print(np.hstack((a, b)))

# 水平组合的另一种写法
print(np.concatenate((a, b), axis=1))  # axis=0的垂直组合

print(np.vstack((a, b)))
print(np.concatenate((a, b), axis=0))

# 深度组合   ==   3维
print(np.dstack((a, b)))
c = np.dstack((a, b))
print(c[1,1,0])

# 列组合 column_stack函数将对一维数组按照列方向进行组合
oned = np.array(range(2))
print(oned)
twice_oned = 2 * oned
print(twice_oned)
print(np.column_stack((oned, twice_oned)))   # 按列方向组合
print(np.column_stack((a, b)))               # 二维数组时将和hstack函数效果相同
print(np.column_stack((a, b)) == np.hstack((a, b)))

print(np.row_stack((oned, twice_oned)))   # 按列方向组合
print(np.row_stack((a, b)))               # 二维数组时将和hstack函数效果相同
print(np.row_stack((a, b)) == np.vstack((a, b)))

# 数组的分割
print("演示水平分割...")
print(a)
print(np.hsplit(a, 3))
print(np.split(a, 3, axis=1))   # 上述分割的另一种写法

print(np.vsplit(a, 3))
print(np.split(a, 3, axis=0))

sx = np.vsplit(a, 3)
print(sx[0])

# 深度分割
c = np.array(range(27)).reshape(3, 3, 3)
print(c)
print(np.dsplit(c, 3))

# 数组的属性
b = np.array(range(24)).reshape(2, 12)
print(b)
print(b.ndim)       # ndim属性为数组维度
print(b.size)
print(b.itemsize)   # 每个元素所占字节大小
print(b.nbytes == b.size * b.itemsize)
b.resize(6, 4)
print(b.reshape(3, 8))   # 使用b.reshape(6, 4)，b并没有发生变化，只是返回的变成6x4的矩阵
print(b.T == np.transpose(b))   # 数组的T属性等价于转置，对于一维数组，其T属性就是原数组

# numpy中复数的虚部是用j表示
b = np.array([1.j + 1, 2.j + 3])
print(b)
print(b.real, b.imag)
print(b.dtype)
print(b.dtype.str)

# flat属性将返回一个numpy.flatiter对象
b = np.array(range(4)).reshape(2, 2)
print(b)
f = b.flat    # 将数组中的数据扁平化，这样可以用for循环遍历数组中的所有元素
for item in f:
    print(item)

print(b.flat[[1,3]])
b.flat = 7   # 还可以赋值，这样原
print(b)
b.flat[[1, 3]] = 1
print(b)

# 数组的转换
b = np.array([1.j + 1, 2.j + 3])
print(b)
print(b.tolist())   
b.astype('complex')
print(b)













