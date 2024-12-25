from collections import Counter

def solution(n, max_sum, array):
    # 统计每个数字出现的次数
    count = Counter(array)
    
    # 找出所有可能的三张相同的牌
    triples = [num for num, freq in count.items() if freq >= 3]
    # 找出所有可能的两张相同的牌
    pairs = [num for num, freq in count.items() if freq >= 2]
    
    # 如果没有足够的牌组成葫芦
    if not triples or len(pairs) < 1:
        return [0, 0]
    
    # 存储合法的葫芦组合
    valid_combinations = []
    
    # 检查所有可能的组合
    for triple in triples:
        for pair in pairs:
            if triple != pair:  # 确保三张牌和两张牌不是同一个数字
                # 计算组合的和
                combination_sum = triple * 3 + pair * 2
                if combination_sum <= max_sum:
                    valid_combinations.append((triple, pair))
    
    # 如果没有合法的组合
    if not valid_combinations:
        return [0, 0]
    
    # 按照规则排序：先比较三张牌（第一个元素），再比较两张牌（第二个元素）
    # 注意：这里要考虑A的特殊情况，A的牌面值为1但大小最大
    def compare_key(combination):
        triple, pair = combination
        # 如果是A（值为1），则赋予最高优先级
        triple_value = float('inf') if triple == 1 else triple
        pair_value = float('inf') if pair == 1 else pair
        return (triple_value, pair_value)
    
    # 获取最大的合法组合
    best_triple, best_pair = max(valid_combinations, key=compare_key)
    
    return [best_triple, best_pair]

if __name__ == "__main__":
    # 测试用例
    print(solution(9, 34, [6, 6, 6, 8, 8, 8, 5, 5, 1]) == [8, 5])
    print(solution(9, 37, [9, 9, 9, 9, 6, 6, 6, 6, 13]) == [6, 9])
    print(solution(9, 40, [1, 11, 13, 12, 7, 8, 11, 5, 6]) == [0, 0])
    print(solution(6, 50, [13, 13, 13, 1, 1, 1]) == [1, 13])
