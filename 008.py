def solution(array):
    # 摩尔投票算法
    candidate = array[0]
    count = 1
    
    # 找出可能的众数
    for num in array[1:]:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    
    # 验证这个数是否真的出现超过一半
    count = sum(1 for x in array if x == candidate)
    if count > len(array) // 2:
        return candidate
    return None


if __name__ == "__main__":
    # 测试用例
    print(solution([1, 3, 8, 2, 3, 1, 3, 3, 3]) == 3)  # 数字3出现5次，超过半数
    print(solution([5, 5, 5, 1, 2, 5, 5]) == 5)        # 数字5出现5次，超过半数
    print(solution([9, 9, 9, 9, 8, 9, 8, 8]) == 9)     # 数字9出现5次，超过半数
