'''
    chap08 质量控制
        numpy testing模块
'''

import numpy as np
import unittest

# assert_almost_equal函数在不同的精度要求下检查两个浮点数是否近似相等
# print("Decimal 6", np.testing.assert_almost_equal(0.123456789, 0.123456780, decimal=7))

# 近似相等，如果两个数字的近似程度没有达到指定的有效数字要求， assert_approx_equal函数将抛出异常
# print("Significance 8", np.testing.assert_approx_equal(0.123456789, 0.123456780, significant=8))

# 核对数组排序，两个数组必须形状一致，并且第一个数组的元素严格小于第二个数组的元素，否则assert_array_less函数将抛出异常
# print("Pass", np.testing.assert_array_less([0, 0.123456789, np.nan], [1, 0.23456780, np.nan]))

# print("Fail", np.testing.assert_array_less([0, 0.123456789, np.nan], [0, 0.23456780, np.nan]))   # 测试不通过

# 比较字符串
print("Pass", np.testing.assert_string_equal("NumPy", "NumPy"))

# print("Fail", np.testing.assert_string_equal("NumPy", "Numpy"))   # 测试不通过

# 浮点数比较
eps = np.finfo(float).eps
print("EPS", eps)
# assert_array_almost_equal_nulp函数比较两个近似相等的浮点数
# print("1", np.testing.assert_array_almost_equal_nulp(1.0, 1.0 + eps))
# print("2", np.testing.assert_array_almost_equal_nulp(1.0, 1.0 + 2 * eps))

# 多ULP的浮点数比较
print("1", np.testing.assert_array_max_ulp(1.0, 1.0 + eps))   # 返回指定ULP数量，以下两个通过测试
print("2", np.testing.assert_array_max_ulp(1.0, 1.0 + 2 * eps, maxulp=2))

# 单元测试
# 单元测试是对代码的一小部分进行自动化测试的单元，通常是一个函数或方法。python中有用于单元测试的PyUnit API

def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        raise ValueError
    return np.arange(1, n + 1).cumprod()

class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(6, factorial(3)[-1])
        np.testing.assert_equal(np.array([1, 2, 6]), factorial(3))

    def test_zero(self):
        self.assertEqual(1, factorial(0))

    def test_negative(self):
        self.assertRaises(IndexError, factorial(-10))

if __name__ == "__main__":
   unittest.main()


# nose和测试装饰器











