## 题目描述
'''
小C手中有一个由小写字母组成的字符串 s。她希望构造另一个字符串 t，并且这个字符串需要满足以下几个条件：

1. t 由小写字母组成，且长度与 s 相同。
2. t 是回文字符串，即从左到右与从右到左读取相同。
3. t 的字典序要小于 s，并且在所有符合条件的字符串中字典序尽可能大。

小C想知道是否能构造出这样的字符串 t，输出这样的t。如果无法构造满足条件的字符串，则输出 -1。
'''

def solution(s):
    n = len(s)
    t = list(s)
    
    # 首先构造一个回文串
    for i in range(n // 2):
        t[n - 1 - i] = t[i]
    
    # 如果构造的回文串已经小于s，直接返回
    if ''.join(t) < s:
        return ''.join(t)
    
    # 从中间向左寻找可以减小的位置
    mid = (n - 1) // 2
    for i in range(mid, -1, -1):
        original_char = t[i]
        if t[i] > 'a':
            # 减小当前位置的字符
            t[i] = chr(ord(t[i]) - 1)
            t[n - 1 - i] = t[i]
            
            # 将i+1到n-i-2的位置都填充'z'
            for j in range(i + 1, n - 1 - i):
                t[j] = 'z'
                
            result = ''.join(t)
            if result < s:
                return result
                
            # 恢复当前位置的字符，继续寻找下一个可能的位置
            t[i] = original_char
            t[n - 1 - i] = original_char
    
    return '-1'


if __name__ == "__main__":
    # 测试样例
    print(solution("abc") == "aba")  # 样例1
    print(solution("cba") == "cac")  # 样例2
    print(solution("aaa") == "-1")   # 样例3
    # 新增测试用例
    print(solution("aaabbbbcaaaccaba") == "aaabbbbbbbbbbaaa")  # 新增测试1
    print(solution("xyz") == "xyx")  # 新增测试2
    print(solution("zzz") == "zyz")  # 新增测试3