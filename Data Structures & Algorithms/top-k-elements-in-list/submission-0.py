class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_elements = Counter(nums)
        print(freq_elements)

        heap = []
        for (num,freq) in freq_elements.items():
            heapq.heappush(heap, (freq,num))

            if(len(heap)>k):
                heapq.heappop(heap)
        print(heap)
        # Extract only the numbers ('num') from the tuples
        result = [num for freq,num in heap]
        return result