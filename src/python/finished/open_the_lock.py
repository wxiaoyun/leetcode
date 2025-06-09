from collections import deque

# https://leetcode.com/problems/open-the-lock/


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        target = (int(target[0]), int(target[1]), int(target[2]), int(target[3]))
        dd = set()
        for d in deadends:
            dd.add((int(d[0]), int(d[1]), int(d[2]), int(d[3])))

        depth = 0
        visited = set()
        q = deque([(0, 0, 0, 0)])
        while q:
            ql = len(q)
            for _ in range(ql):
                comb = q.popleft()
                if comb in visited or comb in dd:
                    continue
                visited.add(comb)

                if comb == target:
                    return depth

                for digit in range(4):
                    tmp = list(comb)
                    original = tmp[digit]

                    tmp[digit] = (original + 1) % 10
                    q.append(tuple(tmp))

                    tmp[digit] = (original - 1) % 10
                    q.append(tuple(tmp))

            depth += 1

        return -1
