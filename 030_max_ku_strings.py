## Problem Description
## Given a string s, which contains only English letters (both uppercase and lowercase).
## Calculate the maximum number of "ku" strings that can be formed from the string.
## Characters are case-insensitive and each character can only be used once.

def solution(s):
    # Convert string to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Count occurrences of 'k' and 'u'
    k_count = s.count('k')
    u_count = s.count('u')
    
    # The number of "ku" strings is limited by the smaller count
    return min(k_count, u_count)

if __name__ == "__main__":
    # Test cases
    print(solution("AUBTMKAxfuu") == 1)  # Sample 1
    print(solution("KKuuUuUuKKKKkkkkKK") == 6)  # Sample 2
    print(solution("abcdefgh") == 0)  # Sample 3