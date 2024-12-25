"""
问题描述：
小U拥有一个由0和1组成的字符串，她可以进行最多k次操作，每次操作可以交换相邻的两个字符。
目标是通过这些操作，使得最终得到的字符串字典序最小。

例如，小U当前有一个字符串 01010，她最多可以进行 2 次相邻字符交换操作。
通过这些操作，她可以将字符串调整为 00101，这是可以通过不超过2次操作得到的字典序最小的字符串。

现在，小U想知道，经过最多k次操作后，能够得到的字典序最小的字符串是什么。
"""

def solution(n, k, s):
    # 将字符串转换为列表以便修改
    s = list(s)
    
    # 对于每个位置，尝试将最小的字符（0）通过k次交换移动到当前位置
    for i in range(n):
        # 在剩余的k次操作内，找到最近的0
        min_pos = i
        for j in range(i + 1, min(i + k + 1, n)):
            if s[j] < s[min_pos]:
                min_pos = j
        
        # 如果找到了更小的字符，进行交换操作
        if min_pos > i:
            # 计算需要的交换次数
            moves = min_pos - i
            if moves <= k:
                # 将找到的字符移动到位置i
                char = s[min_pos]
                for j in range(min_pos, i, -1):
                    s[j] = s[j-1]
                s[i] = char
                # 更新剩余的操作次数
                k -= moves
    
    return ''.join(s)


if __name__ == "__main__":
    # 测试用例1
    print("Test case 1:", solution(5, 2, "01010") == "00101")  # 应该输出 True
    
    # 测试用例2
    print("Test case 2:", solution(7, 3, "1101001") == "0110101")  # 应该输出 True
    
    # 测试用例3
    print("Test case 3:", solution(4, 1, "1001") == "0101")  # 应该输出 True