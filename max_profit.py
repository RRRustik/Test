


prices = [7,1,5,3,6,4]

def maxProfit(prices: list[int]) -> int:
    #def maxProfit(prices):
    # Initialize min_price to a very large value
    min_price = float('inf')
    #print(min_price)
    # Initialize max_profit to 0
    max_profit = 0

    for price in prices:
        #print(price)
        # Update min_price if the current price is lower
        if price < min_price:
            min_price = price
        # Calculate the profit if we sell at the current price
        profit = price - min_price
        # Update max_profit if the current profit is greater
        if profit > max_profit:
            max_profit = profit

    return max_profit

maxProfit([7,1,5,3,6,4])