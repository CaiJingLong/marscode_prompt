"""
问题描述：
小U在一个 m×n 的地图上行走，每个位置有不同高度。移动规则：
1. 只能上坡或下坡，不能走到同高度的点
2. 必须交替上下坡
3. 每个位置只能经过一次
求可以移动的最大次数。
"""

def solution(m, n, grid):
    def dfs(x, y, prev_height, is_up, visited, steps):
        nonlocal max_steps
        max_steps = max(max_steps, steps)
        
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            
            if (new_x < 0 or new_x >= m or 
                new_y < 0 or new_y >= n or 
                (new_x, new_y) in visited):
                continue
            
            curr_height = grid[new_x][new_y]
            if curr_height == prev_height:
                continue
                
            # 检查是否符合上下坡交替条件
            if (is_up and curr_height > prev_height) or (not is_up and curr_height < prev_height):
                continue
                
            visited.add((new_x, new_y))
            dfs(new_x, new_y, curr_height, not is_up, visited, steps + 1)
            visited.remove((new_x, new_y))
    
    max_steps = 0
    # 从每个位置开始尝试，同时尝试上坡和下坡
    for i in range(m):
        for j in range(n):
            dfs(i, j, grid[i][j], True, {(i, j)}, 0)
            dfs(i, j, grid[i][j], False, {(i, j)}, 0)
    
    return max_steps


if __name__ == "__main__":
    # 测试用例
    print(solution(2, 2, [[1, 2], [4, 3]]) == 3)  # True
    print(solution(3, 3, [[10, 1, 6], [5, 9, 3], [7, 2, 4]]) == 8)  # True
    print(solution(4, 4, [[8, 3, 2, 1], 
                         [4, 7, 6, 5], 
                         [12, 11, 10, 9], 
                         [16, 15, 14, 13]]) == 11)  # True
    # 新增测试用例
    print(solution(5, 4, [[3,1,13,3],
                         [13,17,10,11],
                         [13,4,1,15],
                         [3,7,13,17],
                         [8,3,10,16]]) == 12)  # True
