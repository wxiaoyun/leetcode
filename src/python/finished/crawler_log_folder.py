# https://leetcode.com/problems/crawler-log-folder

from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        def move(l: str) -> None:
            match l:
                case "../":
                    if stack:
                        stack.pop()
                case "./":
                    return
                case d:
                    stack.append(d)
        
        for l in logs:
            move(l)
        
        return len(stack)