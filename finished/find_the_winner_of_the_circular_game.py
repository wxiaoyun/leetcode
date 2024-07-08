# https://leetcode.com/problems/find-the-winner-of-the-circular-game

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i+1 for i in range(n)]
        idx = 0
        while len(arr) > 1:
            i = (idx+k-1)%len(arr)
            # print(arr, i)
            popped = arr.pop(i)
            # print(popped)
            idx = i%len(arr)
            # print("new idx: ", idx)
        return arr.pop()
        