class Solution:
    def totalMoney(self, n: int) -> int:
        # 1, 2, 3, 4, 5, 6, 7
        # 2, 3, 4, 5, 6, 7, 8
        # 3, 4, 5, 6, 7, 8, 9
        # 4, 5, 6, 7, 8, 9,10

        daily = [1, 2, 3, 4, 5, 6, 7]
        weekly = sum(daily)

        weeks = n // 7
        rem_days = n % 7

        # money from whole weeks
        total = weeks * weekly
        total += weeks * (weeks - 1) // 2 * 7

        # money from individual days
        total += sum(daily[:rem_days])
        total += weeks * rem_days

        return total
