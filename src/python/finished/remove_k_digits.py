from collections import deque

# https://leetcode.com/problems/remove-k-digits/


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []
        i = 0
        while i < n:
            if k == 0:
                break

            ch = num[i]
            if not stack:
                stack.append(ch)
                i += 1
                continue

            top = stack[-1]
            if ch >= top:
                stack.append(ch)
                i += 1
            else:  # ch < top
                # remove top
                stack.pop()
                k -= 1
        while stack and k > 0:
            stack.pop()
            k -= 1

        result = deque(stack)
        for ch in num[i:]:
            result.append(ch)
        while result and result[0] == "0":
            result.popleft()
        return "".join(result) or "0"
