from typing import List, Tuple

# https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        t_bound = 0
        b_bound = len(matrix) - 1
        l_bound = 0
        r_bound = len(matrix[0]) - 1

        dirs = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]

        def next_cell(i: int, j: int, dir_idx: int) -> Tuple[int, int, int]:
            nonlocal t_bound
            nonlocal r_bound
            nonlocal b_bound
            nonlocal l_bound
            dr, dc = dirs[dir_idx]
            rr, cc = i + dr, j + dc

            if rr < t_bound or rr > b_bound or cc < l_bound or cc > r_bound:
                match dir_idx:
                    case 0:
                        t_bound += 1
                    case 1:
                        r_bound -= 1
                    case 2:
                        b_bound -= 1
                    case 3:
                        l_bound += 1

                return next_cell(i, j, (dir_idx + 1) % 4)

            return rr, cc, dir_idx

        n = len(matrix)
        m = len(matrix[0])

        ans = []
        i, j, dir_idx = 0, -1, 0
        for _ in range(n * m):
            i, j, dir_idx = next_cell(i, j, dir_idx)
            ans.append(matrix[i][j])
        return ans
