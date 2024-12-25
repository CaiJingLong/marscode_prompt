def solution(n, H, A, h, a):
    # 存储可以击败的怪物的索引
    valid_monsters = []
    
    # 筛选出可以击败的怪物
    for i in range(n):
        if h[i] < H and a[i] < A:
            valid_monsters.append((h[i], a[i], i))
    
    if not valid_monsters:
        return 0
    
    # 按照血量和攻击力排序
    valid_monsters.sort()
    m = len(valid_monsters)
    
    # dp[i]表示以第i个怪物结尾的最长递增序列长度
    dp = [1] * m
    
    # 动态规划求解
    for i in range(m):
        for j in range(i):
            if (valid_monsters[i][0] > valid_monsters[j][0] and 
                valid_monsters[i][1] > valid_monsters[j][1] and 
                valid_monsters[i][2] > valid_monsters[j][2]):
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp) if dp else 0

if __name__ == "__main__":
    # 测试用例
    print(solution(3, 4, 5, [1, 2, 3], [3, 2, 1]) == 1)
    print(solution(5, 10, 10, [6, 9, 12, 4, 7], [8, 9, 10, 2, 5]) == 2)
    print(solution(4, 20, 25, [10, 15, 18, 22], [12, 18, 20, 26]) == 3)
    print(solution(4, 20, 25, [22, 18, 15, 10], [26, 20, 18, 12]) == 1)
