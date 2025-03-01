# https://leetcode.com/problems/relative-ranks

import heapq
from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_index = sorted([(sc, i) for i, sc in enumerate(score)], reverse=True)
        result = [None] * len(score)

        for posi, (_, i) in enumerate(score_index):
          result[i] = str(posi+1)

        if len(score) >= 1:
          result[score_index[0][1]] = "Gold Medal"
        if len(score) >= 2:
          result[score_index[1][1]] = "Silver Medal"
        if len(score) >= 3:
          result[score_index[2][1]] = "Bronze Medal"
        return result

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score_index = []
        for i in range(len(score)):
            score_index.append((-score[i], i))
        
        heapq.heapify(score_index)
        output = [None]*len(score)


        place = 1
        while len(score_index) > 0:
            score, i = heapq.heappop(score_index)
            score=-score
            placement = None

            match place:
                case 1:
                    placement = "Gold Medal"
                case 2:
                    placement = "Silver Medal"
                case 3:
                    placement = "Bronze Medal"
                case _:
                    placement = str(place)
            
            output[i] = placement
            place+=1
        
        return output
