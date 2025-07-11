import heapq
from typing import List

# https://leetcode.com/problems/meeting-rooms-iii


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = list(range(n))
        room_use = [0] * n
        finish = []

        meetings = sorted(meetings)
        for s, e in meetings:
            duration = e - s

            while finish and finish[0][0] <= s:
                _, r = heapq.heappop(finish)
                heapq.heappush(free_rooms, r)

            delay = 0
            if not free_rooms:
                ee, r = heapq.heappop(finish)
                delay = max(0, ee - s)
                heapq.heappush(free_rooms, r)

            r = heapq.heappop(free_rooms)
            heapq.heappush(finish, (e + delay, r))
            room_use[r] += 1

        room, room_c = -1, -1
        for r, c in enumerate(room_use):
            if c > room_c:
                room = r
                room_c = c
        return room
