class MedianFinder:

    def __init__(self):
        #contains half of the array and return the last element 
        self.smallMaxHeap = [] 
        #contains the other array half and return the first element
        self.largeMinHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallMaxHeap, -num)

        heapq.heappush(self.largeMinHeap, -heapq.heappop(self.smallMaxHeap))

        if len(self.smallMaxHeap) < len(self.largeMinHeap):
            heapq.heappush(self.smallMaxHeap, -heapq.heappop(self.largeMinHeap))


    def findMedian(self) -> float:
        if len(self.smallMaxHeap) > len(self.largeMinHeap):
            return -self.smallMaxHeap[0]
        else:
            return (-self.smallMaxHeap[0] + self.largeMinHeap[0])/2
        