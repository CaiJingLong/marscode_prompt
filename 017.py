def get_prime_factors(n):
    """获取一个数字的所有素因子"""
    factors = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    return factors

def solution(n, a):
    """
    判断是否可能通过操作使数组中每个元素最多只包含一种素因子
    :param n: 数组长度
    :param a: 输入数组
    :return: 'Yes' 或 'No'
    """
    # 获取每个数的素因子集合
    prime_sets = [get_prime_factors(num) for num in a]
    
    # 统计所有不同的素因子
    all_primes = set()
    for prime_set in prime_sets:
        all_primes.update(prime_set)
    
    # 只要不同素因子的数量不超过数组长度，就一定可以实现
    # 因为可以通过多次操作重新分配素因子
    if len(all_primes) <= n:
        return 'Yes'
    return 'No'

if __name__ == "__main__":
    # 测试用例
    print(solution(4, [1, 2, 3, 4]))     # Yes
    print(solution(2, [10, 12]))         # No
    print(solution(3, [6, 9, 15]))       # Yes
    print(solution(6, [13, 2, 8, 15, 6, 17]))  # Yes
