def maxProfit(self, prices: List[int]) -> int:
    max_profit = 0
    min_num = 10001
    max_num = -1
    for price in prices:
        if price < min_num:
            current_profit = max_num - min_num
            if current_profit > max_profit and max_num >= 0:
                max_profit = current_profit
            min_num = price
            max_num = 0
        elif price > max_num:
            max_num = price            
    current_profit = max_num - min_num
    if current_profit > max_profit and max_num >= 0:
        max_profit = current_profit
    return max_profit
