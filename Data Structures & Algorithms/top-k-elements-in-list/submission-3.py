#revision 1: dated 04 Nov, 2026
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        #print(count)
        result = []
        
        freq = count.most_common(k)
        for key,value in freq:
            result.append(key)
        return result