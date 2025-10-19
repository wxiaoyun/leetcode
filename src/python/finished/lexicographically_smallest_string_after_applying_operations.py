from typing import List

# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        a_cycle = [0]
        cur = a
        while cur != 0:
            a_cycle.append(cur)
            cur = (cur + a) % 10

        n = len(s)
        starting_indices = [0]
        cur = (-b) % n
        while cur != 0:
            starting_indices.append(cur)
            cur = (cur - b) % n

        def find_min_cycle_index(s: str, s_index: int, cycle: List[int]) -> int:
            n = int(s[s_index % len(s)])
            best = n
            best_idx = 0

            for i, delta in enumerate(cycle):
                cur = (n + delta) % 10
                if cur < best:
                    best = cur
                    best_idx = i

            return best_idx

        def get_cycled_num(
            s: str,
            start: int,
            off_set: int,
            cycle: List[int],
            even_cycle: int,
            odd_cycle: int,
        ) -> int:
            s_idx = (start + off_set) % len(s)
            cycle_idx = even_cycle if off_set % 2 == 0 else odd_cycle
            return (int(s[s_idx]) + cycle[cycle_idx]) % 10

        b_odd = (b % 2) == 1  # if b is odd, we can apply a to all indices

        best_start, best_even_cycle, best_odd_cycle = 0, 0, 0
        for start in starting_indices:
            even_cycle = find_min_cycle_index(s, start, a_cycle) if b_odd else 0
            odd_cycle = find_min_cycle_index(s, start + 1, a_cycle)

            # lexicographic string comparison
            for i in range(n):
                cur_num = get_cycled_num(s, start, i, a_cycle, even_cycle, odd_cycle)
                best_num = get_cycled_num(
                    s, best_start, i, a_cycle, best_even_cycle, best_odd_cycle
                )

                if cur_num > best_num:
                    break
                if cur_num == best_num:
                    continue

                # cur_num < best_num
                best_start = start
                best_even_cycle = even_cycle
                best_odd_cycle = odd_cycle
                break

        ans = []
        for i in range(n):
            best_num = get_cycled_num(
                s, best_start, i, a_cycle, best_even_cycle, best_odd_cycle
            )
            ans.append(str(best_num))
        return "".join(ans)
