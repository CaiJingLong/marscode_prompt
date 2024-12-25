"""
问题描述：
小C希望构造一个包含n个元素的数组，且满足以下条件：
1. 数组中的所有元素两两不同
2. 数组所有元素的最大公约数为 k
3. 数组元素之和尽可能小

要求：输出该数组元素之和的最小值
"""

from math import gcd
from functools import reduce

def solution(n, k):
    # 如果k是1，我们可以直接使用最小的n个正整数
    if k == 1:
        return sum(range(1, n + 1))
    
    # 如果k > 1，我们需要找到最小的n个互不相同的k的倍数
    result = []
    num = k
    while len(result) < n:
        result.append(num)
        num += k
    
    return sum(result)


if __name__ == "__main__":
    # 测试用例1：n = 3, k = 1
    print(solution(3, 1) == 6)  # 1 + 2 + 3 = 6
    
    # 测试用例2：n = 2, k = 2
    print(solution(2, 2) == 6)  # 2 + 4 = 6
    
    # 测试用例3：n = 4, k = 3
    print(solution(4, 3) == 30)  # 3 + 6 + 9 + 12 = 30