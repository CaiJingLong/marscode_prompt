def solution(n, m, s, c):
    # 统计货架上每种商品的数量
    shelf_items = {}
    for item in s:
        shelf_items[item] = shelf_items.get(item, 0) + 1
    
    # 统计每个位置能卖出多少商品
    sales = 0
    used_items = set()  # 记录已经使用过的商品
    
    # 遍历每个顾客需求
    for customer_need in c:
        # 如果货架上有这个商品，且还未被使用
        if customer_need in shelf_items and shelf_items[customer_need] > 0:
            # 放置商品并更新统计
            shelf_items[customer_need] -= 1
            sales += 1
    
    return sales

if __name__ == "__main__":
    # 测试用例
    print(solution(3, 4, "abc", "abcd") == 3)  # 可以按 "abc" 排列，卖出3件
    print(solution(4, 2, "abbc", "bb") == 2)   # 可以按 "bbac" 排列，卖出2件
    print(solution(5, 4, "bcdea", "abcd") == 4)  # 可以按 "abcde" 排列，卖出4件
