## Problem Description
# Given a string word consisting of digits and lowercase English letters, replace every non-digit character with a space.
# Then, count the number of different integers remaining after the replacement.
# Two integers are considered different if their decimal representations without leading zeros are different.

def solution(word):
    # Replace non-digit characters with spaces
    replaced = ''.join([c if c.isdigit() else ' ' for c in word])
    
    # Split into individual number strings and convert to integers
    numbers = [int(num) for num in replaced.split()]
    
    # Return count of unique numbers
    return len(set(numbers))


if __name__ == "__main__":
    # Test cases
    print(solution("a123bc34d8ef34") == 3)  # True
    print(solution("t1234c23456") == 2)     # True
    print(solution("a1b01c001d4") == 2)     # True