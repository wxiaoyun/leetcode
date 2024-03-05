# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while (left < right):
            left_char = s[left]
            right_char = s[right]

            if (left_char != right_char):
                break

            # trim left
            while (s[left] == left_char ):
                if left >= right:
                    return 0
                left += 1

            # trim right
            while (s[right] == right_char):
                if left >= right:
                    return 0
                right -= 1

        return right - left + 1

