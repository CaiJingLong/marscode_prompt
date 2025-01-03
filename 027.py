"""
问题描述：
小U在一款挂机游戏中拥有n个英雄。游戏中有一种历练升级机制，每天可以选择两个英雄进行历练，
如果两位英雄的等级相同，则他们的等级都不会改变。如果英雄等级不同，那么等级较高的英雄会增加1级，
而等级较低的英雄则保持不变。小U希望至少有一个英雄能够达到2000000000000000级，
他想知道有多少英雄有潜力通过历练达到这个等级。
"""

def solution(n, u):
    # 如果所有英雄等级都相同，则无法升级
    if len(set(u)) == 1:
        return 0
    
    # 获取最小等级
    min_level = min(u)
    
    # 计算除了最小等级外的所有英雄数量
    return n - u.count(min_level)


if __name__ == "__main__":
    # Test cases
    print(solution(5, [1, 2, 3, 1, 2]) == 3)  # 除了两个等级1的英雄，其他都可以升级
    print(solution(4, [100000, 100000, 100000, 100000]) == 0)  # 所有英雄等级相同，无法升级
    print(solution(6, [1, 1, 1, 2, 2, 2]) == 3)  # 除了三个等级1的英雄，其他都可以升级
