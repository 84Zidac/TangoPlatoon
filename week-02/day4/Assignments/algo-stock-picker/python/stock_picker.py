
def picker(prices):
    best_profit = 0
    buy_index = 0
    sell_index = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > best_profit:
                best_profit = profit
                buy_index = i
                sell_index = j
    return [buy_index, sell_index]






