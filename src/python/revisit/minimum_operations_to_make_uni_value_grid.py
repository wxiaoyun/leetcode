import numpy as np

class Solution:
    def minOperations(self, grid, x):
        nums_array = np.array(grid).reshape(-1)
        nums_array.sort()
        final_common_number = nums_array[len(nums_array) // 2]

        if ((nums_array % x) - (final_common_number % x)).any():
            return -1
        
        return int((np.abs(nums_array * -1 + final_common_number) // x).sum())