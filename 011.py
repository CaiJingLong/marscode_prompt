def solution(values):
    max_score = 0
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            score = values[i] + values[j] + i - j
            if score > max_score:
                max_score = score
    return max_score

if __name__ == "__main__":
    print(solution([8, 3, 5, 5, 6]) == 11)
    print(solution([10, 4, 8, 7]) == 16)
    print(solution([1, 2, 3, 4, 5]) == 8)
