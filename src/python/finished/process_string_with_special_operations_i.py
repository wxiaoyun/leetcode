import copy
from collections import deque

# https://leetcode.com/problems/process-string-with-special-operations-i/


class Solution:
    def processStr(self, s: str) -> str:
        L2R, R2L = False, True
        dir = L2R
        result = deque()

        for cmd in s:
            match cmd:
                case "*":
                    if dir == L2R and result:
                        result.pop()
                    elif result:
                        result.popleft()
                case "#":
                    result_cp = copy.deepcopy(result)
                    if dir == L2R:
                        result.extend(result_cp)
                    else:
                        result_cp.reverse()
                        result.extendleft(result_cp)
                case "%":
                    dir = not dir
                case ch:
                    if dir == L2R:
                        result.append(ch)
                    else:
                        result.appendleft(ch)

        if dir == R2L:
            result.reverse()
        return "".join(result)
