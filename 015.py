"""
问题描述：
小U和小R有两个字符串，分别是S和T，现在小U需要通过对S进行若干次操作，使其变成T的一个前缀。
操作可以是修改S的某一个字符，或者删除S末尾的字符。
现在你需要帮助小U计算出，最少需要多少次操作才能让S变成T的前缀。
"""

def solution(S: str, T: str) -> int:
    # 如果S已经是T的前缀，不需要操作
    if T.startswith(S):
        return 0
    
    # 如果S比T长，需要删除多余的字符，并且可能需要修改一些字符
    if len(S) > len(T):
        # 需要删除的字符数
        delete_count = len(S) - len(T)
        # 需要修改的字符数
        modify_count = sum(1 for i in range(len(T)) if S[i] != T[i])
        return delete_count + modify_count
    
    # 如果S比T短或等长，只需要计算需要修改的字符数
    return sum(1 for i in range(len(S)) if S[i] != T[i])


if __name__ == "__main__":
    # 测试用例
    print("测试用例1:", solution("aba", "abb") == 1)  # 修改最后一个字符
    print("测试用例2:", solution("abcd", "efg") == 4)  # 修改三个字符并删除一个字符
    print("测试用例3:", solution("xyz", "xy") == 1)  # 删除最后一个字符
    print("测试用例4:", solution("hello", "helloworld") == 0)  # 已经是前缀
    print("测试用例5:", solution("same", "same") == 0)  # 完全相同
