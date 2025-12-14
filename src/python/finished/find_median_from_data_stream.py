import heapq


class MedianFinder:
    def __init__(self):
        # invariant:
        # 1. all elements in left heap are smaller than or equals to
        #   the minimum element of the right heap
        # 2. | len(left) - len(right) | <= 1
        self.left_max = []
        self.right_min = []

    def addNum(self, num: int) -> None:
        # we always add the num to the left max_heap
        heapq.heappush(self.left_max, -num)

        # if the size of left heap is greater by more than one than the right heap
        # it is imbalanced
        if len(self.left_max) > len(self.right_min) + 1:
            lmax = -heapq.heappop(self.left_max)
            heapq.heappush(self.right_min, lmax)

        # we check and maintain the invariant that all elements on the left
        # is smaller than or equals to min element of the right
        if self.right_min and (-self.left_max[0]) > self.right_min[0]:
            lmax = -heapq.heappop(self.left_max)
            rmin = heapq.heappop(self.right_min)

            heapq.heappush(self.left_max, -rmin)
            heapq.heappush(self.right_min, lmax)

        assert len(self.left_max) - len(self.right_min) <= 1

    def findMedian(self) -> float:
        if len(self.left_max) > len(self.right_min):
            return -self.left_max[0]

        lmax = -self.left_max[0]
        rmin = self.right_min[0]
        return lmax + (rmin - lmax) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
