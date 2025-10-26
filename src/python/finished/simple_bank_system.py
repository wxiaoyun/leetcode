from typing import List

# https://leetcode.com/problems/simple-bank-system/


class Bank:
    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        a1, a2 = account1 - 1, account2 - 1
        if min(a1, a2) < 0 or max(a1, a2) >= self.n:
            return False

        if self.balance[a1] < money:
            return False

        self.balance[a1] -= money
        self.balance[a2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        a = account - 1
        if a < 0 or a >= self.n:
            return False

        self.balance[a] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        a = account - 1
        if a < 0 or a >= self.n:
            return False

        if self.balance[a] < money:
            return False

        self.balance[a] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
