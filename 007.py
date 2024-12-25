def solution(n, template, titles):
    # 将模板按照 {} 分割成固定部分
    def parse_template(template):
        parts = []
        i = 0
        while i < len(template):
            start = i
            # 找到下一个 {
            while i < len(template) and template[i] != '{':
                i += 1
            if i > start:
                parts.append(template[start:i])
            if i < len(template):
                # 跳过 {
                i += 1
                # 找到对应的 }
                while i < len(template) and template[i] != '}':
                    i += 1
                i += 1  # 跳过 }
                parts.append(None)  # None 表示通配符位置
        return parts

    def match_title(parts, title):
        if not parts:
            return len(title) == 0

        if parts[0] is None:
            # 当前是通配符，尝试不同长度的匹配
            for i in range(len(title) + 1):
                if match_title(parts[1:], title[i:]):
                    return True
            return False
        else:
            # 当前是固定字符串，必须匹配
            if not title.startswith(parts[0]):
                return False
            return match_title(parts[1:], title[len(parts[0]):])

    # 解析模板
    template_parts = parse_template(template)
    
    # 处理每个标题
    results = []
    for title in titles:
        results.append(str(match_title(template_parts, title)))
    
    return ','.join(results)

if __name__ == "__main__":
    # 测试用例
    print(solution(4, "ad{xyz}cdc{y}f{x}e", ["adcdcefdfeffe", "adcdcefdfeff", "dcdcefdfeffe", "adcdcfe"]) == "True,False,False,True")
    print(solution(3, "a{bdc}efg", ["abcdefg", "abefg", "efg"]) == "True,True,False")
    print(solution(5, "{abc}xyz{def}", ["xyzdef", "abcdef", "abxyzdef", "xyz", "abxyz"]) == "True,False,True,True,True")
