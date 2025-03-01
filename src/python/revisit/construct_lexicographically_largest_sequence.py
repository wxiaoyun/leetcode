from typing import List

# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        N = n * 2 - 1
        res = [0] * N
        used = [False] * (n + 1)

        def build(i: int) -> bool:
            if i >= N:
                return True
            
            if res[i]:
                return build(i + 1)
            
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                
                j = i + num
                used[num] = True

                if num == 1:
                    res[i] = num
                    if build(i + 1):
                        return True
                    res[i] = 0
                elif j < N and not res[j]:
                    res[i], res[j] = num, num
                    if build(i + 1):
                        return True
                    res[i], res[j] = 0, 0
                
                used[num] = False

            return False                

        build(0)
        return res

            
