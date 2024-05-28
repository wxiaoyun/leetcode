# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        delta = [(n^k)-n for n in nums]
        delta.sort(key=lambda x: -x)

        _sum = sum(nums)

        for j in range(0, len(delta), 2):
            if j+1 == len(delta):
                break
            
            d = delta[j]
            dd = delta[j+1]

            if d + dd > 0:
                _sum += d
                _sum += dd
            else:
                break
        
        return _sum
