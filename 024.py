"""
问题描述：
小R有一个特殊的随机播放规则。他首先播放歌单中的第一首歌，播放后将其从歌单中移除。
如果歌单中还有歌曲，则会将当前第一首歌移到最后一首。这个过程会一直重复，直到歌单中没有任何歌曲。

样例 1：
输入：n = 5, a = [5, 3, 2, 1, 4]
输出：[5, 2, 4, 1, 3]

样例 2：
输入：n = 4, a = [4, 1, 3, 2]
输出：[4, 3, 1, 2]

样例 3：
输入：n = 6, a = [1, 2, 3, 4, 5, 6]
输出：[1, 3, 5, 2, 6, 4]
"""

def solution(n, a):
    # 使用列表模拟队列
    queue = a.copy()
    result = []
    
    while queue:
        # 播放并移除第一首歌
        result.append(queue.pop(0))
        
        # 如果队列还有歌，将第一首移到末尾
        if queue:
            queue.append(queue.pop(0))
    
    return result

if __name__ == "__main__":
    # 测试用例
    print(solution(5, [5, 3, 2, 1, 4]) == [5, 2, 4, 1, 3])  # True
    print(solution(4, [4, 1, 3, 2]) == [4, 3, 1, 2])  # True
    print(solution(6, [1, 2, 3, 4, 5, 6]) == [1, 3, 5, 2, 6, 4])  # True
