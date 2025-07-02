# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit


class Solution:
    def minMaxDifference(self, num: int) -> int:
        min_val = list(str(num))
        first = min_val[0]
        for i in range(len(min_val)):
            if min_val[i] == first:
                min_val[i] = "0"
        min_val = int("".join(min_val))

        max_val = list(str(num))
        first = None
        for i in range(len(max_val)):
            if not first and max_val[i] != "9":
                first = max_val[i]

            if first and max_val[i] == first:
                max_val[i] = "9"
        max_val = int("".join(max_val))

        return max_val - min_val
