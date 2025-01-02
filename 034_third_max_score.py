## 题目描述
'''
小M想要通过查看往届游戏比赛的排名来确定自己比赛的目标分数。他希望找到往届比赛中排名第三的分数，作为自己的目标。具体规则如下：

如果分数中有三个或以上不同的分数，返回其中第三大的分数。
如果不同的分数只有两个或更少，那么小M将选择最大的分数作为他的目标。
'''

def solution(n, nums):
    # 去重并排序
    unique_nums = sorted(list(set(nums)), reverse=True)
    
    # 判断不同分数的数量
    if len(unique_nums) >= 3:
        return unique_nums[2]
    else:
        return unique_nums[0]

if __name__ == "__main__":
    # 测试用例
    print(solution(3, [3, 2, 1]) == 1)  # 样例1
    print(solution(2, [1, 2]) == 2)     # 样例2
    print(solution(4, [2, 2, 3, 1]) == 1)  # 样例3
    # 额外测试用例
    print(solution(4, [5, 5, 5, 5]) == 5)  # 所有分数相同
    print(solution(6, [9, 8, 7, 6, 5, 4]) == 7)  # 多个不同分数
    print(solution(1, [1]) == 1)  # 只有一个分数