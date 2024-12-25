def solution(n, k, data):
    # 初始化dp数组，设置一个较大的初始值
    INF = float('inf')
    dp = [[INF] * (k + 1) for _ in range(n)]
    
    # 处理第一天的情况
    for buy in range(k + 1):
        dp[0][buy-1] = data[0] * buy
    
    # 遍历每一天
    for i in range(1, n):
        # 遍历当天可能剩余的食物数量
        for j in range(k):
            if dp[i-1][j] == INF:
                continue
            # 当天需要购买的食物数量范围
            max_buy = k - j
            # 遍历购买的可能性
            for buy in range(max_buy + 1):
                next_food = j + buy - 1  # 减1是因为要消耗这一天的食物
                if next_food >= 0:
                    dp[i][next_food] = min(dp[i][next_food], 
                                         dp[i-1][j] + buy * data[i])
    
    return dp[n-1][0] if dp[n-1][0] != INF else -1

if __name__ == "__main__":
    # 测试用例
    print(solution(5, 2, [1, 2, 3, 3, 2]) == 9)
    print(solution(6, 3, [4, 1, 5, 2, 1, 3]) == 9)
    print(solution(4, 1, [3, 2, 4, 1]) == 10)
