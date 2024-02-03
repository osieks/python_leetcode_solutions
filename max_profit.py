from typing import List


def maxProfit(prices: List[int]) -> int:
    buy=0
    buy_working=0
    sell=0
    
    for i in range(len(prices)):
        if prices[i]<prices[buy]:
            buy=i
            sell=i
        if prices[i]-prices[buy]>=0:
            if prices[i]>prices[sell]:
                sell=i
                #buy_working=buy
    if(buy>sell):
        buy = buy_working
    
    print(prices[sell],prices[buy])
    return prices[sell]-prices[buy]
        
from typing import List

def maxProfit2(prices: List[int]) -> int:
    if not prices:
        return 0
    
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    
    return max_profit

print(maxProfit2([2,4,1]))
print(maxProfit2([7,1,5,3,6,4]))
print(maxProfit2([7,6,4,3,1]))