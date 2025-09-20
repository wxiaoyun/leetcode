from collections import defaultdict, deque
from typing import List, Set, Tuple

# https://leetcode.com/problems/implement-router/


class Router:

    def __init__(self, memoryLimit: int):
        self.mem_limit = memoryLimit
        self.packets: Set[Tuple[int, int, int]] = set()
        self.packet_by_dest = defaultdict(deque)
        self.packet_deque = deque()

    def evict_one(self) -> List[int]:
        if len(self.packet_deque) == 0:
            return []

        old_packet = self.packet_deque.popleft()
        self.packets.remove(old_packet)
        old_packet_dest = old_packet[1]
        self.packet_by_dest[old_packet_dest].popleft()
        return old_packet

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packets:
            return False

        if len(self.packets) == self.mem_limit:
            self.evict_one()

        self.packet_deque.append(key)
        self.packets.add(key)
        self.packet_by_dest[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        return self.evict_one()

    def binary_search(self, dest: int, timestamp: int) -> int:
        dq = self.packet_by_dest[dest]
        l, r = 0, len(dq)
        ans = r
        while l < r:
            m = l + (r - l) // 2
            t = dq[m]

            if t < timestamp:
                l = m + 1
            else:
                ans = m
                r = m
        # return left most index that satisfy the condition: t >= timestamp
        return ans

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        l = self.binary_search(destination, startTime)
        r = self.binary_search(destination, endTime + 1)
        return r - l


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
