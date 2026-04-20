class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        countNums = Counter(nums)
        large = -1
        for num in countNums:
            if countNums[num] == 1:
                large = max(large, num)
        
        return large