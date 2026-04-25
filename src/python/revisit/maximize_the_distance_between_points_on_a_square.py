from typing import List

# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # (a, 0) -> a
        # (side, b) -> side + b
        # (c, side) -> 3 * side - c
        # (0, d) -> 3 * d + d

        pts = []
        for c, r in points:
            if c == 0:
                pts.append(r)
            elif r == side:
                pts.append(side + c)
            elif c == side:
                pts.append(3 * side - r)
            elif r == 0:
                pts.append(4 * side - c)
            else:
                raise Exception("unreachable")

        n = len(pts)
        L = 4 * side
        pts.sort()
        # print(pts)
        # print()

        # Duplicate the array to handle cyclic wrap-around easily
        A = pts + [p + L for p in pts]

        def possible(guess: int) -> bool:
            # nxt array: nxt[i] will store the index of the closest point >= guess distance away
            # We pad it to 2 * n + 1 so out-of-bounds jumps safely land on 2 * n
            nxt = [2 * n] * (2 * n + 1)
            j = 0

            # 1. Precompute all `nxt` valid jumps using two pointers (O(N) time)
            for i in range(2 * n):
                j = max(j, i + 1)  # Ensure we always move forward to distinct points
                while j < 2 * n and A[j] - A[i] < guess:
                    j += 1
                nxt[i] = j

            # 2. Check if any starting point allows k-1 valid jumps (O(N * K) time)
            for i in range(n):
                curr = i
                for _ in range(k - 1):
                    curr = nxt[curr]
                    # If we ran out of available points, this starting point fails
                    if curr >= 2 * n:
                        break
                else:
                    # The `else` triggers only if the loop completed without breaking.
                    # We check if the distance from the first to the last point fits in our perimeter budget
                    if A[curr] - A[i] <= L - guess:
                        return True

            return False

        ans = -1
        l, r = 0, (4 * side) // k + 1
        while l < r:
            m = l + (r - l) // 2
            if possible(m):
                ans = m
                l = m + 1
            else:
                r = m

        return ans


# TLE
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # (a, 0) -> a
        # (side, b) -> side + b
        # (c, side) -> 3 * side - c
        # (0, d) -> 3 * d + d

        pts = []
        for c, r in points:
            if c == 0:
                pts.append(r)
            elif r == side:
                pts.append(side + c)
            elif c == side:
                pts.append(3 * side - r)
            elif r == 0:
                pts.append(4 * side - c)
            else:
                raise Exception("unreachable")

        pts.sort()
        # print(pts)
        # print()

        def possible(guess: int) -> bool:
            kprev = pts[:]
            kcnt = [1] * len(pts)
            # can we find k points such that the maximum MMD is `guess`?
            # we try to arrange the k points into a line,

            for i in pts:
                for j in range(len(pts)):
                    # kprev[j] <-------> i <-----> (-guess + i) % k
                    #           >=guess    >=guess
                    if i - kprev[j] >= guess and i <= pts[j] + (4 * side) - guess:
                        kprev[j] = i
                        kcnt[j] += 1

            # print(guess)
            # print(kprev)
            # print(kcnt)
            # print()

            return any(cnt >= k for cnt in kcnt)

        ans = -1
        l, r = 0, (4 * side) // k + 1
        while l < r:
            m = l + (r - l) // 2
            if possible(m):
                ans = m
                l = m + 1
            else:
                r = m

        return ans
