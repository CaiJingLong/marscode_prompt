"""
问题描述：
小R正在组织一个比赛，比赛中有 n 支队伍参赛。比赛遵循以下独特的赛制：

如果当前队伍数为 偶数，那么每支队伍都会与另一支队伍配对。总共进行 n / 2 场比赛，且产生 n / 2 支队伍进入下一轮。
如果当前队伍数为 奇数，那么将会随机轮空并晋级一支队伍，其余的队伍配对。总共进行 (n - 1) / 2 场比赛，且产生 (n - 1) / 2 + 1 支队伍进入下一轮。

小R想知道在比赛中进行的配对次数，直到决出唯一的获胜队伍为止。
"""

def solution(n):
    if n <= 1:
        return 0
    
    total_matches = 0
    remaining_teams = n
    
    while remaining_teams > 1:
        if remaining_teams % 2 == 0:
            # 偶数队伍的情况
            matches = remaining_teams // 2
            remaining_teams = matches
        else:
            # 奇数队伍的情况
            matches = (remaining_teams - 1) // 2
            remaining_teams = matches + 1
        
        total_matches += matches
    
    return total_matches


if __name__ == "__main__":
    # 测试用例1
    print(solution(7) == 6)  # True
    
    # 测试用例2
    print(solution(14) == 13)  # True
    
    # 测试用例3
    print(solution(1) == 0)  # True
    
    # 额外测试用例
    print(solution(8) == 7)  # True
