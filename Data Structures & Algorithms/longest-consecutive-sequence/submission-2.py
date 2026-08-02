class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        numSet = set(nums)
        longest = 0
        for i in range(len(nums)):
            
            if (nums[i] - 1) not in numSet:
                currentNum = nums[i]
                currentLength = 1
            
                while (currentNum + 1) in numSet:
                    currentNum += 1
                    currentLength += 1
            
                longest = max(currentLength, longest)
        
        return longest


