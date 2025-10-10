from typing import List

# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        best = -float("inf")

        j = 0
        energies = [0] * k
        for e in reversed(energy):
            new_energy = energies[j] + e
            energies[j] = new_energy
            best = max(best, new_energy)
            j = (j + 1) % k
        return best
