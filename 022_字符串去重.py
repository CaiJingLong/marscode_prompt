"""
问题描述：
小U得到一个只包含小写字母的字符串 S。她可以执行如下操作：
每次选择字符串中两个相同的字符删除，然后在字符串末尾添加一个任意的小写字母。
小U想知道，最少需要多少次操作才能使得字符串中的所有字母都不相同？
"""

def solution(S):
    # 统计每个字符的出现次数
    char_count = {}
    for c in S:
        char_count[c] = char_count.get(c, 0) + 1
    
    operations = 0
    
    while True:
        # 检查是否还有重复字符
        max_count = max(char_count.values()) if char_count else 0
        if max_count <= 1:
            break
            
        # 找到一个重复次数最多的字符
        for char, count in char_count.items():
            if count > 1:
                # 删除两个相同字符
                char_count[char] -= 2
                if char_count[char] == 0:
                    del char_count[char]
                
                # 添加一个未使用的字符
                for new_char in 'abcdefghijklmnopqrstuvwxyz':
                    if new_char not in char_count:
                        char_count[new_char] = 1
                        break
                
                operations += 1
                break
    
    return operations


if __name__ == "__main__":
    # 测试用例1
    print(solution("abab") == 2)  # True
    
    # 测试用例2
    print(solution("aaaa") == 2)  # True
    
    # 测试用例3
    print(solution("abcabc") == 3)  # True
