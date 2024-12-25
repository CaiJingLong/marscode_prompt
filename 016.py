"""
问题描述：
小S最近在分析一个数组，数组的每个元素代表某种高度。小S对这些高度感兴趣的是，当我们选取任意 k 个相邻元素时，
如何计算它们所能形成的最大矩形面积。

对于 k 个相邻的元素，我们定义其矩形的最大面积为：
R(k) = k × min(h[i], h[i+1], ..., h[i+k−1])
即，R(k) 的值为这 k 个相邻元素中的最小值乘以 k。
现在，小S希望你能帮他找出对于任意 k，R(k) 的最大值。
"""

def solution(n, array):
    # 遍历所有可能的k（从1到n）
    max_area = 0
    
    # 对于每个k，计算所有可能的k个相邻元素的最大矩形面积
    for k in range(1, n + 1):
        # 遍历所有可能的起始位置
        for i in range(n - k + 1):
            # 计算当前k个相邻元素中的最小值
            min_height = min(array[i:i + k])
            # 计算面积
            area = k * min_height
            max_area = max(max_area, area)
    
    return max_area


if __name__ == "__main__":
    # Test case 1
    print(solution(5, [1, 2, 3, 4, 5]) == 9)  # True
    
    # Test case 2
    print(solution(6, [5, 4, 3, 2, 1, 6]) == 9)  # True
    
    # Test case 3
    print(solution(4, [4, 4, 4, 4]) == 16)  # True
