"""
问题描述：
小R正在研究DNA序列，他需要一个函数来计算将一个受损DNA序列（dna1）转换成一个未受损序列（dna2）
所需的最少编辑步骤。编辑步骤包括：增加一个碱基、删除一个碱基或替换一个碱基。
"""

def solution(dna1, dna2):
    m, n = len(dna1), len(dna2)
    
    # 创建dp数组
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 初始化边界条件
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # 填充dp数组
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if dna1[i-1] == dna2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,    # 删除
                    dp[i][j-1] + 1,    # 插入
                    dp[i-1][j-1] + 1   # 替换
                )
    
    return dp[m][n]

if __name__ == "__main__":
    # 测试用例
    print(solution("AGT", "AGCT") == 1)          # True
    print(solution("AACCGGTT", "AACCTTGG") == 4) # True
    print(solution("ACGT", "TGC") == 3)          # True
    print(solution("A", "T") == 1)               # True
    print(solution("GGGG", "TTTT") == 4)         # True
