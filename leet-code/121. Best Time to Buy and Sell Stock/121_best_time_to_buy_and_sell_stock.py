def max_profit(prices):
    min_num = 10 ^ 4 + 1
    profit = 0

    for price in prices:
        min_num = min(min_num, price)
        profit = max(profit, price - min_num)

    return profit


print(max_profit([7, 1, 5, 3, 6, 4]))
# 5
print(max_profit([7, 6, 4, 3, 1]))
# 0
print(max_profit([4, 3, 2, 7, 6, 5]))
# 5
