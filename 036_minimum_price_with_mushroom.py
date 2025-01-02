## 题目描述
'''
小C来到了一家饭馆，这里共有 n 道菜，第 i 道菜的价格为 a_i。其中一些菜中含有蘑菇，s_i 代表第 i 道菜是否含有蘑菇。如果 s_i = '1'，那么第 i 道菜含有蘑菇，否则没有。
小C希望点 k 道菜，且希望总价格尽可能低。由于她不喜欢蘑菇，她希望所点的菜中最多只有 m 道菜含有蘑菇。小C想知道在满足条件的情况下能选出的最小总价格是多少。如果无法按照要求选择菜品，则输出-1。
'''

def solution(s, a, m, k):
    # 将菜分为含蘑菇和不含蘑菇两类
    mushroom = []
    no_mushroom = []
    for i in range(len(s)):
        if s[i] == '1':
            mushroom.append(a[i])
        else:
            no_mushroom.append(a[i])
    
    # 对两类菜分别排序
    mushroom.sort()
    no_mushroom.sort()
    
    # 预处理前缀和
    prefix_m = [0] * (len(mushroom) + 1)
    for i in range(len(mushroom)):
        prefix_m[i+1] = prefix_m[i] + mushroom[i]
    
    prefix_nm = [0] * (len(no_mushroom) + 1)
    for i in range(len(no_mushroom)):
        prefix_nm[i+1] = prefix_nm[i] + no_mushroom[i]
    
    # 遍历所有可能的含蘑菇菜的数量（0到m）
    min_total = float('inf')
    for i in range(min(m, len(mushroom)) + 1):
        j = k - i
        if j < 0 or j > len(no_mushroom):
            continue
        total = prefix_m[i] + prefix_nm[j]
        if total < min_total:
            min_total = total
    
    return min_total if min_total != float('inf') else -1


if __name__ == "__main__":
    # 测试样例
    print(solution("001", [10, 20, 30], 1, 2) == 30)  # 样例1
    print(solution("111", [10, 20, 30], 1, 2) == -1)  # 样例2
    print(solution("0101", [5, 15, 10, 20], 2, 3) == 30)  # 样例3