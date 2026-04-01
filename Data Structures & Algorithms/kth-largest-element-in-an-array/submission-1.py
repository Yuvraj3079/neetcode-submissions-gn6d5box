class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-num for num in nums]
        heapq.heapify(maxheap)
        ans = 0
        while k:
            ans = heapq.heappop(maxheap)
            k -= 1
        
        return -(ans)