# For a given number, lookup the smallest index.
# The challenge here is that the smallest index may change when we perform a change operation
# and the changed number was the smallest index.
# We need an efficient way to find the second smallest index for that same number
#
# If the workload is read heavy, the optimal approach will be using a heap to keep track of 
# minimum index with O(1) lookup for minimum. But maintaining the heap on change can cost O(nlogn)
#
# If the workload is write heavy, the optimal approach will be using a hashmap to keep
# track of the number at each index. Writes will be O(1), but reads will cost O(n) where
# a full scan of the hashmap is required.


from collections import defaultdict
import heapq


class NumberContainers:
    def __init__(self):
        self.index2num = {}
        self.num_pq = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index2num:
            n = self.index2num[index]
            self.delete(index, n)
        self.index2num[index] = number
        
        if number not in self.num_pq:
            self.num_pq[number] = {
                "dirty": False,
                "set": set(),
                "pq": list()
            }
        
        ds = self.num_pq[number]
        ds["set"].add(index)
        heapq.heappush(ds["pq"], index)
        # print(f"CHANGE i: {index}, n: {number}")
        # print(self.index2num)
        # print(self.num_pq)
        
    def find(self, number: int) -> int:
        if number not in self.num_pq:
            return -1
        
        ds = self.num_pq[number]
        if len(ds["set"]) == 0:
            return -1
        
        if ds["dirty"]:
            pq = list(ds["set"])
            heapq.heapify(pq)

            ds["pq"] = pq
            ds["dirty"] = False
        
        # print(f"FIND n: {number}")
        # print(self.num_pq)
        return ds["pq"][0]

    def delete(self, index: int, number: int) -> None:
        ds = self.num_pq[number]
        ds["set"].remove(index)
        ds["dirty"] = True
        # print(f"DELETE i: {index}, n: {number}")
        # print(self.index2num)
        # print(self.num_pq)


# TLE for write heavy workload
class NumberContainers:
    def __init__(self):
        self.num_pq = defaultdict(list)
        self.index2num = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index2num:
            num = self.index2num[index]
            self.delete(index, num)
        self.index2num[index] = number
        
        heapq.heappush(self.num_pq[number], index)
        # print("CHANGE", index, number)
        # print(self.num_pq)
        # print(self.index2num)
        
    def find(self, number: int) -> int:
        # print("FIND", number)
        if number not in self.num_pq:
            return -1
        if len(self.num_pq[number]) == 0:
            return -1
        return self.num_pq[number][0]
        
    def delete(self, index: int, number: int) -> None:
        # print("DELETE", index, number)
        pq = self.num_pq[number]

        for i, n in enumerate(pq):
            if n != index:
                continue
            
            pq[i] = pq[-1] # copy last element to ith position
            pq.pop() # remove the last element
            heapq.heapify(pq)


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)