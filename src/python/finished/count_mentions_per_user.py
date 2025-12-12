import heapq

from typings import List

# https://leetcode.com/problems/count-mentions-per-user/


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events = [
            (int(time), 1 if ty == "OFFLINE" else 2, ty, payload)
            for ty, time, payload in events
        ]
        heapq.heapify(events)

        is_online = {uid: True for uid in range(numberOfUsers)}
        mentions = [0] * numberOfUsers
        all_cnt = 0
        while events:
            time, _, ty, payload = heapq.heappop(events)

            match ty:
                case "OFFLINE":
                    uid = int(payload)
                    is_online[uid] = False
                    heapq.heappush(events, (time + 60, 0, "ON", uid))
                case "ON":
                    uid = int(payload)
                    is_online[uid] = True
                case "MESSAGE":
                    if payload == "ALL":
                        all_cnt += 1
                    elif payload == "HERE":
                        for uid, online in is_online.items():
                            if not online:
                                continue
                            mentions[uid] += 1
                    else:
                        ids = payload.split(" ")
                        for id_str in ids:
                            uid = int(id_str[2:])
                            mentions[uid] += 1

        return [m + all_cnt for m in mentions]
