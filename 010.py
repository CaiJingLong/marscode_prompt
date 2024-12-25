def solution(a, b):
    # Calculate the minimum number of days to break even
    return a // b if a % b == 0 else a // b + 1

if __name__ == "__main__":
    # Test cases
    print(solution(10, 1) == 10)
    print(solution(10, 2) == 5)
    print(solution(10, 3) == 4)
