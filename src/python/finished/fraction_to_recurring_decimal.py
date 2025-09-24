# https://leetcode.com/problems/fraction-to-recurring-decimal/


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        digits = []
        if numerator * denominator < 0:
            digits.append("-")
        numerator = abs(numerator)
        denominator = abs(denominator)

        dividend_index_lookup = {}
        dividend = numerator
        divisor = denominator
        first_time_cross_one = True
        while True:
            if dividend in dividend_index_lookup:
                digits.insert(dividend_index_lookup[dividend], "(")
                digits.append(")")
                return "".join(digits)

            if not first_time_cross_one:
                dividend_index_lookup[dividend] = len(digits)

            if dividend % divisor == 0:
                digits.append(str(dividend // divisor))
                return "".join(digits)

            if dividend < divisor:
                digits.append("0")
            else:
                quotient = dividend // divisor
                remainder = dividend % divisor

                digits.append(str(quotient))
                dividend = remainder

            if dividend < divisor and first_time_cross_one:
                digits.append(".")
                first_time_cross_one = False
                dividend_index_lookup[dividend] = len(digits)
            dividend *= 10

        return ""
