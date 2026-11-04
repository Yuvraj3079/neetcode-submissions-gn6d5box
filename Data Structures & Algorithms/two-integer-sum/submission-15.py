class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        mapToNumber = {}

        for i, val in enumerate(nums):

            complement = target - val
            
            if complement in mapToNumber:
                return [mapToNumber[complement], i]
            mapToNumber[val] = i
        return []
            

