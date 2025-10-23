from typing import List
import heapq

# https://leetcode.com/problems/number-of-orders-in-the-backlog/


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        sell_min_hp = []
        buy_max_hp = []

        def process_buy(price: int, amount: int):
            while sell_min_hp:
                sell_price, sell_amt = sell_min_hp[0]
                if sell_price > price:
                    break

                sell_price, sell_amt = heapq.heappop(sell_min_hp)
                exchange_amount = min(amount, sell_amt)

                sell_amt -= exchange_amount
                amount -= exchange_amount

                if sell_amt > 0:
                    heapq.heappush(sell_min_hp, (sell_price, sell_amt))

                if amount == 0:
                    return

            heapq.heappush(buy_max_hp, (-price, amount))

        def process_sell(price: int, amount: int):
            while buy_max_hp:
                buy_price, buy_amt = buy_max_hp[0]
                buy_price *= -1
                if buy_price < price:
                    break

                buy_price, buy_amt = heapq.heappop(buy_max_hp)
                buy_price *= -1
                exchange_amount = min(amount, buy_amt)

                buy_amt -= exchange_amount
                amount -= exchange_amount

                if buy_amt > 0:
                    heapq.heappush(buy_max_hp, (-buy_price, buy_amt))

                if amount == 0:
                    return

            heapq.heappush(sell_min_hp, (price, amount))

        BUY = 0
        SELL = 1
        for p, a, ty in orders:
            if ty == BUY:
                process_buy(p, a)
            elif ty == SELL:
                process_sell(p, a)

        left_amount = 0
        MOD = int(1e9) + 7
        for _, a in sell_min_hp:
            left_amount = (left_amount + a) % MOD
        for _, a in buy_max_hp:
            left_amount = (left_amount + a) % MOD
        return left_amount
