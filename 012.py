"""
问题描述：
小S有一个由字符 'U' 和 'C' 组成的字符串 S，并希望在编辑距离不超过给定值 m 的条件下，
尽可能多地在字符串中找到 "UCC" 子串。

编辑距离定义为将字符串 S 转化为其他字符串时所需的最少编辑操作次数。
允许的每次编辑操作是插入、删除或替换单个字符。

约束条件：
- 字符串长度不超过1000
"""

def solution(m, s):
    n = len(s)
    
    def get_max_ucc(pos, edits, last_used=-1, memo=None):
        if memo is None:
            memo = {}
            
        if edits < 0:
            return float('-inf')
            
        # 当到达字符串末尾时，考虑剩余编辑次数能创建多少个UCC
        if pos >= n:
            return edits // 3
            
        state = (pos, edits, last_used)
        if state in memo:
            return memo[state]
            
        result = 0
        
        # 1. 跳过当前位置
        result = max(result, get_max_ucc(pos + 1, edits, last_used, memo))
        
        # 2. 在当前位置尝试创建UCC
        # 2.1 使用现有字符并修改/插入缺失字符
        if pos + 2 < n and pos > last_used:
            edit_cost = 0
            if s[pos] != 'U':
                edit_cost += 1
            if s[pos + 1] != 'C':
                edit_cost += 1
            if s[pos + 2] != 'C':
                edit_cost += 1
            if edit_cost <= edits:
                result = max(result, 1 + get_max_ucc(pos + 3, edits - edit_cost, pos + 2, memo))
        
        # 2.2 在当前位置插入完整的UCC
        if edits >= 3 and pos > last_used:
            result = max(result, 1 + get_max_ucc(pos, edits - 3, pos - 1, memo))
        
        # 2.3 利用当前字符，插入部分字符形成UCC
        if pos > last_used:
            # 如果当前是U，可以插入CC
            if pos < n and s[pos] == 'U' and edits >= 2:
                result = max(result, 1 + get_max_ucc(pos + 1, edits - 2, pos, memo))
                
            # 如果当前是C，可以插入UC
            if pos < n and s[pos] == 'C' and edits >= 2:
                result = max(result, 1 + get_max_ucc(pos + 1, edits - 2, pos, memo))
                
            # 如果有UC，可以插入C
            if pos + 1 < n and s[pos] == 'U' and s[pos + 1] == 'C' and edits >= 1:
                result = max(result, 1 + get_max_ucc(pos + 2, edits - 1, pos + 1, memo))
        
        # 2.4 考虑删除当前字符
        if edits >= 1:
            result = max(result, get_max_ucc(pos + 1, edits - 1, last_used, memo))
            
        # 2.5 考虑在当前位置之前插入字符
        if edits >= 1 and pos > last_used:
            # 插入U（如果后面有CC）
            if pos + 1 < n and s[pos] == 'C' and s[pos + 1] == 'C':
                result = max(result, 1 + get_max_ucc(pos + 2, edits - 1, pos + 1, memo))
            # 插入C（如果前面刚好是UC）
            if pos > 0 and s[pos - 1] == 'U' and s[pos] == 'C' and pos - 1 > last_used:
                result = max(result, 1 + get_max_ucc(pos + 1, edits - 1, pos, memo))
        
        memo[state] = result
        return result
    
    return get_max_ucc(0, m)


if __name__ == "__main__":
    # 测试用例1
    print(solution(3, "UCUUCCCCC") == 3)  # True
    
    # 测试用例2
    print(solution(6, "U") == 2)  # True
    
    # 测试用例3
    print(solution(2, "UCCUUU") == 2)  # True
    
    # 测试用例4
    print(solution(10, "CCU") == 4)  # True
    
    # 测试用例5
    print(solution(3, "CUUUCUCUUUUCU") == 3)  # True
    
    # 测试用例6
    print(solution(7, "CCUUUCUCU") == 5)  # True