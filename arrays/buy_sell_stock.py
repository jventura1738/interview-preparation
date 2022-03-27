# Justin Ventura

from typing import List


# Best time to buy and sell stock:
def buy_sell_stock(prices: List[int] = None) -> int:
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        curr_amount = price - min_price
        max_profit = max(curr_amount, max_profit)
        min_price = min(min_price, price)

    return max_profit


if __name__ == '__main__':
    result = buy_sell_stock([7, 1, 5, 3, 6, 4])
    assert result == 5
    print(result)
