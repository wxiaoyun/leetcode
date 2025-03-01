# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        def sort_by_first_coord(p: List[list]) -> int:
            return p[0]
        
        # first sort points by starting coord
        sorted_pts = sorted(points, key=sort_by_first_coord)

        shots = 0
        i = 0 # index of next unshot balloon

        while i < len(sorted_pts):
            shots += 1 # Fire a shot at the current ballon
            shot_right_bound = sorted_pts[i][1]

            # See whether this shot can hit other ballons
            while i < len(sorted_pts):
                # check if there is overlap between balloon i and j
                if not sorted_pts[i][0] <= shot_right_bound:
                    break
                
                # There is overlap, we need to contract the overlap
                # Contract right boundery to the minimum right boundery
                shot_right_bound = min(shot_right_bound, sorted_pts[i][1])
                i += 1
            
        return shots

