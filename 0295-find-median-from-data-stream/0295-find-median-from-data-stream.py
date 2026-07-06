import heapq

class MedianFinder(object):

    def __init__(self):
        # Max Heap (store negative values)
        self.small = []

        # Min Heap
        self.large = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        # Add to max heap
        heapq.heappush(self.small, -num)

        # Move largest element to min heap
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance the heaps
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """
        :rtype: float
        """

        # If odd number of elements
        if len(self.small) > len(self.large):
            return float(-self.small[0])

        # If even number of elements
        return (-self.small[0] + self.large[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian())   # 1.5
# obj.addNum(3)
# print(obj.findMedian())   # 2.0