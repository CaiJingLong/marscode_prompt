def solution(numbers):
    # 将每个数字转换为数字列表
    digit_groups = []
    for num in numbers:
        # 将整数转换为字符串，然后提取unique数字
        num_str = str(num)
        group = []
        for digit in num_str:
            if digit not in group:  # 避免重复数字
                group.append(int(digit))
        digit_groups.append(group)
    
    def is_sum_even(combination):
        return sum(combination) % 2 == 0
    
    def generate_combinations(groups, current_combination=[]):
        if not groups:  # 基本情况：已经处理完所有组
            if is_sum_even(current_combination):
                return 1
            return 0
            
        count = 0
        current_group = groups[0]
        remaining_groups = groups[1:]
        
        for digit in current_group:
            count += generate_combinations(remaining_groups, 
                                        current_combination + [digit])
        
        return count
    
    return generate_combinations(digit_groups)


if __name__ == "__main__":
    # 测试用例 - 现在使用整数而不是字符串
    print(solution([123, 456, 789]) == 14)  # True
    print(solution([123456789]) == 4)  # True
    print(solution([14329, 7568]) == 10)  # True
