"""
问题描述：
在一个 N × M 的竞技场迷宫中，找出所有的"危险位置"的数量。
"危险位置"定义为：如果站在该位置上，无论采取什么移动策略，都无法到达出口。

竞技场元素：
.：普通地板，可以上下左右移动
O：出口
U：向上传送器
D：向下传送器
L：向左传送器
R：向右传送器
"""

def find_exit(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 'O':
                return i, j
    return -1, -1

def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def get_next_position(x, y, cell, N, M):
    """处理传送器的传送效果"""
    if cell == 'U':
        return (x-1, y) if x > 0 else (-1, -1)
    elif cell == 'D':
        return (x+1, y) if x < N-1 else (-1, -1)
    elif cell == 'L':
        return (x, y-1) if y > 0 else (-1, -1)
    elif cell == 'R':
        return (x, y+1) if y < M-1 else (-1, -1)
    return (x, y)

def solution(N, M, data):
    # 找到出口位置
    exit_x, exit_y = find_exit(data)
    
    # 记录可以到达出口的位置
    safe = [[False] * M for _ in range(N)]
    safe[exit_x][exit_y] = True
    
    # 使用队列进行BFS
    queue = [(exit_x, exit_y)]
    changed = True
    
    while changed:
        changed = False
        # 遍历所有位置
        for x in range(N):
            for y in range(M):
                if safe[x][y]:
                    continue
                    
                # 检查当前位置是否可以到达安全位置
                can_reach_safe = False
                cell = data[x][y]
                
                if cell == '.':
                    # 普通地板，检查四周
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if is_valid(nx, ny, N, M) and safe[nx][ny]:
                            can_reach_safe = True
                            break
                else:
                    # 传送器，检查传送后的位置
                    nx, ny = get_next_position(x, y, cell, N, M)
                    if nx != -1 and safe[nx][ny]:
                        can_reach_safe = True
                
                if can_reach_safe:
                    safe[x][y] = True
                    changed = True
    
    # 计算危险位置的数量
    danger_count = sum(1 for i in range(N) for j in range(M) if not safe[i][j])
    return danger_count


if __name__ == "__main__":
    # 测试用例1
    data1 = [
        [".", ".", ".", ".", "."],
        [".", "R", "R", "D", "."],
        [".", "U", ".", "D", "R"],
        [".", "U", "L", "L", "."],
        [".", ".", ".", ".", "O"]
    ]
    print(solution(5, 5, data1) == 10)  # True
    
    # 测试用例2
    data2 = [
        [".", "R", ".", "O"],
        ["U", ".", "L", "."],
        [".", "D", ".", "."],
        [".", ".", "R", "D"]
    ]
    print(solution(4, 4, data2) == 2)  # True
    
    # 测试用例3
    data3 = [
        [".", "U", "O"],
        ["L", ".", "R"],
        ["D", ".", "."]
    ]
    print(solution(3, 3, data3) == 8)  # True
