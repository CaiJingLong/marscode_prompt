## 这个各种AI都通不过

## 题目写在代码的注释中
"""
问题描述
小F面临一个有趣的挑战：给定一个数组，她需要将数组中的数字分为两组。分组的目标是使得一组数字的和的个位数等于给定的 A，另一组数字的和的个位数等于给定的 B。
除此之外，还有一种特殊情况允许其中一组为空，但剩余数字和的个位数必须等于 A 或 B。小F需要计算所有可能的划分方式。

测试样例
样例1：
输入：n = 3, A = 1, B = 2, array_a = [1, 1, 1]
输出：3

样例2：
输入：n = 3, A = 3, B = 5, array_a = [1, 1, 1]
输出：1

样例3：
输入：n = 2, A = 1, B = 1, array_a = [1, 1]
输出：2

样例4：
输入：n = 5, A = 3, B = 7, array_a = [2, 3, 5, 7, 9]
输出：0
"""

from itertools import combinations

def solution(n, A, B, array_a):
    total_ways = 0
    total_sum = sum(array_a)

    # 遍历所有可能的子集
    for i in range(len(array_a) + 1):
        for subset in combinations(array_a, i):
            subset_sum = sum(subset)
            other_sum = total_sum - subset_sum

            # 检查是否满足条件
            if (subset_sum % 10 == A and other_sum % 10 == B) or \
               (subset_sum % 10 == B and other_sum % 10 == A):
                total_ways += 1

    # 特殊情况：其中一组为空
    if total_sum % 10 == A or total_sum % 10 == B:
        total_ways += 1

    return total_ways


if __name__ == "__main__":
    # 测试样例1
    print(solution(3, 1, 2, [1, 1, 1]) == 3)  # 输出：3
    
    # 测试样例2
    print(solution(3, 3, 5, [1, 1, 1]) == 1)  # 输出：1
    
    # 测试样例3
    print(solution(2, 1, 1, [1, 1]) == 2)  # 输出：2
    
    # 测试样例4
    print(solution(5, 3, 7, [2, 3, 5, 7, 9]) == 0)  # 输出：0
