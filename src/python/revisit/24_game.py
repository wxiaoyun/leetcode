from typing import List


class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        eps = 1e-6

        def generate(nums: List[int]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < eps

            for i in range(len(nums)):
                a = nums[i]
                for j in range(i + 1, len(nums)):
                    b = nums[j]

                    evl = [a + b, a * b, a - b, b - a]
                    if a != 0:
                        evl.append(b / a)
                    if b != 0:
                        evl.append(a / b)

                    rest = [n for k, n in enumerate(nums) if k not in [i, j]]
                    for v in evl:
                        rest.append(v)
                        if generate(rest):
                            return True
                        rest.pop()

            return False

        return generate(cards)
