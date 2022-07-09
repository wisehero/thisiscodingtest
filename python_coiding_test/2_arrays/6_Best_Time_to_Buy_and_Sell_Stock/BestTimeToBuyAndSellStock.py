"""
한 번의 거래로 낼 수 있는 최대 이익을 산출하라.

Input: prices = [7,1,5,3,6,4]
Output: 5
"""
import sys


def maxProfit(prices):
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit
