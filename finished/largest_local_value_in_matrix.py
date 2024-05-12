# https://leetcode.com/problems/largest-local-values-in-a-matrix

import numpy as np
from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        mat = np.array(grid)
        result = []

        for i in range(len(grid)-2):
            row = []
            result.append(row)
            for j in range(len(grid[0])-2):
                window = mat[i:i+3,j:j+3]
                flat = window.reshape((-1))
                row.append(np.max(flat))
        
        return result
                
        
