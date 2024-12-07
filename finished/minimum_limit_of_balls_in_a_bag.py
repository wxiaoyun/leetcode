from typing import List

# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        total = sum(nums)
        partitions = len(nums) + maxOperations
        l = total // partitions
        r = max(nums)

        def is_possible(maxOperations: int, guess: int) -> bool:
          if guess == 0:
            return False
          operations = 0

          for n in nums:
            if n <= guess:
              continue

            # n / d = m
            # n = md
            # d = n / m
            # 5 / 2 => 2.5 (2) (3) (5-1)//2 + 1 = 3
            # 2 / 1 => 2 (2) (2) (2-1)//1 + 1 = 2
            operations += (n-1) // guess + 1 - 1 # minus 1 because we are considering additional splits only
            if operations > maxOperations:
              return False

          return True
        
        while l < r:
          m = (r - l) // 2 + l

          if is_possible(maxOperations, m):
            r = m
          else:
            l = m + 1
        return l

    # def minimumSize(self, nums: List[int], maxOperations: int) -> int:
    #     pq = [(-n, n, 1) for n in nums]
    #     heapq.heapify(pq)
    #     # print(pq)

    #     for _ in range(maxOperations):
    #         _, val, freq = heapq.heappop(pq)
    #         freq += 1
    #         heapq.heappush(pq, (-val/freq, val, freq))
    #         # print(pq)
    #     val, _, _ = heapq.heappop(pq)
    #     return math.ceil(-val)