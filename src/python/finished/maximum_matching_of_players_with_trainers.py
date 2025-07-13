from typing import List

# https://leetcode.com/problems/maximum-matching-of-players-with-trainers


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # Each trainer should train the player with the highest ability lte its capacity

        players, trainers = sorted(players), sorted(trainers)
        i = len(players) - 1
        count = 0
        for cap in reversed(trainers):
            while i >= 0 and players[i] > cap:
                i -= 1
            if i < 0:
                break
            count += 1
            i -= 1
        return count
