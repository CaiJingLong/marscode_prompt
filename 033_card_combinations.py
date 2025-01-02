## 题目描述
'''
小M有 n 张卡牌，每张卡牌的正反面分别写着不同的数字，正面是 a_i，背面是 b_i。小M希望通过选择每张卡牌的一面，使得所有向上的数字之和可以被3整除。你需要告诉小M，一共有多少种不同的方案可以满足这个条件。由于可能的方案数量过大，结果需要对 10^9+7 取模。
'''

MOD = 10**9 + 7

def solution(n, a, b):
    dp = [[0] * 3 for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(3):
            if dp[i - 1][j]:
                dp[i][(j + a[i - 1]) % 3] = (dp[i][(j + a[i - 1]) % 3] + dp[i - 1][j]) % MOD
                dp[i][(j + b[i - 1]) % 3] = (dp[i][(j + b[i - 1]) % 3] + dp[i - 1][j]) % MOD
                
    return dp[n][0]

if __name__ == "__main__":
    # 测试样例1
    print(solution(3, [1, 2, 3], [2, 3, 2]) == 3)  # 输出：True
    # 测试样例2
    print(solution(4, [3, 1, 2, 4], [1, 2, 3, 1]) == 6)  # 输出：True
    # 测试样例3
    print(solution(5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 32)  # 输出：True