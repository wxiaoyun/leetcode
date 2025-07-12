# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer


class Solution:
    def maxDiff(self, num: int) -> int:
        chrs = list(str(num))
        if len(set(chrs)) == 1:
            min_val = int("1" * len(chrs))
        else:
            replace = None
            replace_with = None
            first = chrs[0]
            for i in range(len(chrs)):
                if not replace:
                    if i == 0 and chrs[i] != "1":
                        replace = chrs[i]
                        replace_with = "1"
                    elif i > 0 and chrs[i] != "0" and chrs[i] != first:
                        replace = chrs[i]
                        replace_with = "0"

                if replace and chrs[i] == replace:
                    chrs[i] = replace_with
            min_val = int("".join(chrs))

        chrs = list(str(num))
        replace = None
        for i in range(len(chrs)):
            if not replace and chrs[i] != "9":
                replace = chrs[i]
            if replace and chrs[i] == replace:
                chrs[i] = "9"
        max_val = int("".join(chrs))

        return max_val - min_val
