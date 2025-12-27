import heapq
from typing import List

# https://leetcode.com/problems/meeting-rooms-iii


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        MEETING_END = 0
        MEETING_START = 1

        meeting_cnt = [0] * n
        free_rooms = list(range(n))
        wait_list = []
        events = [(s, MEETING_START, i) for i, (s, e) in enumerate(meetings)]
        heapq.heapify(events)

        while events:
            t, ty, payload = heapq.heappop(events)

            match ty:
                case ty if ty == MEETING_END:
                    room_id = payload

                    if wait_list:
                        # if wait list is not empty, pass the room
                        s, e = heapq.heappop(wait_list)
                        duration = e - s

                        heapq.heappush(events, (t + duration, MEETING_END, room_id))
                        meeting_cnt[room_id] += 1
                    else:
                        # else mark room as free
                        heapq.heappush(free_rooms, room_id)

                case ty if ty == MEETING_START:
                    idx = payload
                    _, e = meetings[idx]

                    if not free_rooms:
                        # if no free rooms, push to wait list
                        heapq.heappush(wait_list, (t, e))
                    else:
                        # else consume a free room
                        room_id = heapq.heappop(free_rooms)

                        heapq.heappush(events, (e, MEETING_END, room_id))
                        meeting_cnt[room_id] += 1

        max_cnt = 0
        room_id = -1
        for id, cnt in enumerate(meeting_cnt):
            if cnt > max_cnt:
                room_id = id
                max_cnt = cnt
        return room_id


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = list(range(n))
        room_use = [0] * n
        finish = []

        meetings = sorted(meetings)
        for s, e in meetings:
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
