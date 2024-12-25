def solution(s):
    # 分离整数和小数部分
    parts = s.split('.')
    
    # 处理整数部分（去除前导零）
    integer_part = parts[0].lstrip('0')
    if not integer_part:  # 如果整数部分为空（即原数为0开头）
        integer_part = '0'
    
    # 从右向左每三位添加逗号
    formatted_integer = ''
    for i, digit in enumerate(integer_part[::-1]):
        if i > 0 and i % 3 == 0:
            formatted_integer = ',' + formatted_integer
        formatted_integer = digit + formatted_integer
    
    # 如果有小数部分，则添加小数部分
    if len(parts) > 1:
        return formatted_integer + '.' + parts[1]
    return formatted_integer


if __name__ == "__main__":
    # 测试用例
    print(solution("1294512.12412") == '1,294,512.12412')  # True
    print(solution("0000123456789.99") == '123,456,789.99')  # True
    print(solution("987654321") == '987,654,321')  # True
