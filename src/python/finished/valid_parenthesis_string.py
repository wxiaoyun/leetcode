from collections import deque

# https://leetcode.com/problems/valid-parenthesis-string/


class Solution:
    def checkValidString(self, s: str) -> bool:
        # In the simple case without wildcards, we can keep track of count of left brackets.
        # Every time we encounter "(", we increment the count
        # Every time we encounter ")", we try to decrement the count. If there count is zero, then its invalid

        # Now we have wildcards, if we encounter ")" and there is insufficient "(", we can consume the wildcard

        wildcards = deque()
        lstack = []
        for i, ch in enumerate(s):
            match ch:
                case "*":
                    wildcards.append(i)
                case "(":
                    lstack.append(i)
                case ")":
                    if lstack:
                        lstack.pop()
                    elif not wildcards:
                        return False
                    else:
                        wildcards.popleft()

        while lstack:
            if not wildcards or wildcards[-1] < lstack[-1]:
                return False

            lstack.pop()
            wildcards.pop()

        return True
