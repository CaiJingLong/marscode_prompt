"""
问题描述：
小S正在玩一个关于石子的游戏，给定了一些石子，它们位于一维数轴的不同位置，位置用数组 stones 表示。
如果某个石子处于最小或最大的一个位置，我们称其为端点石子。
在每个回合，小S可以将一颗端点石子移动到一个未占用的位置，使其不再是端点石子。
游戏继续，直到石子的位置变得连续，无法再进行任何移动操作。
你需要帮助小S找到可以移动的最大次数。
"""

def solution(stones: list) -> int:
    stones.sort()
    N = len(stones)
    total_empty_positions = stones[-1] - stones[0] + 1 - N
    left_gap = stones[1] - stones[0] - 1 if N > 1 else 0
    right_gap = stones[-1] - stones[-2] - 1 if N > 1 else 0
    min_end_gap = min(left_gap, right_gap)
    max_moves = total_empty_positions - min_end_gap
    return max_moves


if __name__ == "__main__":
    # 测试用例1
    print(solution([7, 4, 9]) == 2)  # True
    
    # 测试用例2
    print(solution([6, 5, 4, 3, 10]) == 3)  # True
    
    # 测试用例3
    print(solution([1, 2, 3, 4, 5]) == 0)  # True
    
    # 测试用例4
    print(solution([12, 15, 7, 2, 13]) == 8)  # True
    
    # 测试用例5 - 两个石子的情况
    print(solution([12, 4]) == 0)  # True
    
    # 测试用例6 - 新的测试用例
    print(solution([3, 1, 8, 13, 9]) == 7)  # True
