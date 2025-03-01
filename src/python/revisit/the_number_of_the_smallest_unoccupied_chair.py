from heapq import heappop, heappush
from typing import List

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

# class Solution:
#     def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
#         events = []
#         for p, pair in enumerate(times):
#           ar, lv = pair
#           events.extend([(ar, p, True), (lv, p, False)])
#         # print(events)
#         def comp(a, b):
#           ta, _, ba = a
#           tb, _, bb = b
#           if ta == tb and ba != bb:
#             return -1 if not ba else 1
#           return ta - tb
#         events = sorted(events, key=functools.cmp_to_key(comp))
#         # print(events)

#         seat_occupied = defaultdict(bool)
#         p_to_seat = {}

#         for _, p, is_ar in events:
#           if is_ar:
#             seat = 0
#             while True:
#               if not seat_occupied[seat]:
#                 # print("Person", p, "occupying", seat)
#                 if p == targetFriend:
#                   return seat
#                 seat_occupied[seat] = True
#                 p_to_seat[p] = seat
#                 break
#               seat += 1
#             continue

#           # is leaving
#           seat = p_to_seat[p]
#           del p_to_seat[p]
#           seat_occupied[seat] = False
#           # print("Person", p, "leaving", seat)

#         return -1


