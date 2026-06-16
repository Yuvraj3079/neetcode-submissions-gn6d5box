#revision 1: dated 16 June, 2026

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in prevMap:
                return [prevMap[diff], i]
            
            prevMap[num] = i