# https://leetcode.com/problems/hand-of-straights

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand)%groupSize) != 0:
            return False
        
        hand.sort()
        used = -1

        def find_and_consume(start_idx: int, target: int) -> bool:
            for i in range(start_idx, len(hand)):
                if hand[i] == target:
                    hand[i] = used
                    return True

            return False

        for i in range(len(hand)):
            if hand[i] == used:
                continue
            
            for j in range(1, groupSize):
                found = find_and_consume(i+j, hand[i]+j)
                if not found:
                    return False
            
            hand[i] = used
        
        for n in hand:
            if not n == used:
                return False

        return True