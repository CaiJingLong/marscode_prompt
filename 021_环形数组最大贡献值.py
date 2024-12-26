"""
问题描述：
小S拿到了一个长度为 n 的环形数组，并定义了两个下标 i 和 j 的贡献值公式为：
f(i, j) = (a_i + a_j) × dist(i, j)，其中 dist(i, j) 是下标 i 和 j 在数组中的最短距离。
小S希望找到一对下标，使得它们的贡献值尽可能大。环形数组的特点是最左和最右的元素也是相邻的。
"""

def solution(n, a):
    max_contribution = 0
    for i in range(n):
        for j in range(i + 1, n):  # 优化：只需要遍历i后面的元素
            # 计算环形数组中的最短距离
            dist = min(abs(i - j), n - abs(i - j))
            # 计算贡献值
            contribution = (a[i] + a[j]) * dist
            max_contribution = max(max_contribution, contribution)
    return max_contribution


if __name__ == "__main__":
    # 测试用例1
    print(solution(3, [1, 2, 3]) == 5)  # True
    
    # 测试用例2
    print(solution(4, [4, 1, 2, 3]) == 12)  # True
    
    # 测试用例3
    print(solution(5, [1, 5, 3, 7, 2]) == 24)  # True
