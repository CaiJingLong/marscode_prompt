## Problem Description
# Given a string consisting of 'a', 'b', and 'c' characters, perform k transformations where:
# 'a' → 'bc'
# 'b' → 'ca'
# 'c' → 'ab'
# Return the final transformed string

def solution(s, k):
    # Create transformation mapping
    transform = {'a': 'bc', 'b': 'ca', 'c': 'ab'}
    
    # Perform k transformations
    for _ in range(k):
        new_s = []
        for char in s:
            new_s.append(transform[char])
        s = ''.join(new_s)
    
    return s


if __name__ == "__main__":
    # Test case 1
    print(solution("abc", 2) == "caababbcbcca")  # True
    
    # Test case 2
    print(solution("abca", 3) == "abbcbccabccacaabcaababbcabbcbcca")  # True
    
    # Test case 3
    print(solution("cba", 1) == "abcabc")  # True