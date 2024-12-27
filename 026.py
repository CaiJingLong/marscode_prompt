"""
问题描述：
小U手中有两个数字 a 和 b。第一个数字是一个任意的正整数，而第二个数字是一个非负整数。
她的任务是将第二个数字 b 插入到第一个数字 a 的某个位置，以形成一个最大的可能数字。

样例 1：
输入：a = 76543, b = 4
输出：765443
解释：将4插入到6和5之间可以得到最大数字

样例 2：
输入：a = 1, b = 0
输出：10
解释：只能将0插入到1的后面

样例 3：
输入：a = 44, b = 5
输出：544
解释：将5插入到开头可以得到最大数字

样例 4：
输入：a = 666, b = 6
输出：6666
解释：将6插入到任意位置都可以得到相同的结果
"""

def solution(a, b):
    # 将数字转换为字符串
    str_a = str(a)
    str_b = str(b)
    
    # 存储所有可能的结果
    results = []
    
    # 尝试在每个位置插入b
    for i in range(len(str_a) + 1):
        # 在位置i插入b
        new_num = int(str_a[:i] + str_b + str_a[i:])
        results.append(new_num)
    
    # 返回最大结果
    return max(results)

if __name__ == "__main__":
    # 测试用例
    print(solution(76543, 4) == 765443)  # True
    print(solution(1, 0) == 10)          # True
    print(solution(44, 5) == 544)        # True
    print(solution(666, 6) == 6666)      # True
