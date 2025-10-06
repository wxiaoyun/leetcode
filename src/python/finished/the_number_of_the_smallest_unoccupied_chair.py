from heapq import heappop, heappush
from typing import List

# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        LEAVE = 0
        ARRIVE = 1
        events = [None] * (2 * len(times))
        for f, (arr, lea) in enumerate(times):
            events[2 * f] = (lea, LEAVE, f)
            events[2 * f + 1] = (arr, ARRIVE, f)
        events.sort()

        # Goal: find efficient way to retrieve smallest available chair
        friend_to_chair = {}
        free_chairs = []
        n_chair = 0
        for t, ty, f in events:
            if ty == LEAVE:
                chair = friend_to_chair[f]
                del friend_to_chair[f]
                heapq.heappush(free_chairs, chair)
                continue

            # ty == ARRIVE:
            chair = -1
            if not free_chairs:
                chair = n_chair
                n_chair += 1
            else:
                chair = heapq.heappop(free_chairs)

            if f == targetFriend:
                return chair

            friend_to_chair[f] = chair

        return -1


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        events = []
        for p, pair in enumerate(times):
            ar, lv = pair
            events.extend([(ar, p, True), (lv, p, False)])
        events = sorted(events)

        av_seats = [i for i in range(len(times))]
        oc_seats = []

        for t, p, is_arr in events:
            while oc_seats and oc_seats[0][0] <= t:
                _, seat = heappop(oc_seats)
                heappush(av_seats, seat)

            if is_arr:
                seat = heappop(av_seats)
                if p == targetFriend:
                    return seat
                heappush(oc_seats, (times[p][1], seat))

        return -1
