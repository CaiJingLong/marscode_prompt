"""
问题描述：
小U得到了一个数字n，他的任务是构造一个特定数组。这个数组的构造规则是：
对于每个i从1到n，将数字n到i逆序拼接，直到i等于n为止。
最终，输出这个拼接后的数组。

例如，当n等于3时，拼接后的数组是 [3, 2, 1, 3, 2, 3]。
"""

def solution(n):
    result = []
    # 从1到n遍历
    for i in range(1, n + 1):
        # 对于每个i，添加从n到i的数字
        for j in range(n, i - 1, -1):
            result.append(j)
    return result


if __name__ == "__main__":
    # Test case 1
    print(solution(3) == [3, 2, 1, 3, 2, 3])
    
    # Test case 2
    print(solution(4) == [4, 3, 2, 1, 4, 3, 2, 4, 3, 4])
    
    # Test case 3
    print(solution(5) == [5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5])