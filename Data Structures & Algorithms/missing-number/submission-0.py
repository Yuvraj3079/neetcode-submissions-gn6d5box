class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumN = (n*(n + 1))//2
        print(sumN)
        sum = 0
        for num in nums:
            sum += num
        
        if sum == sumN:
            return 0
        else:
            return (sumN - sum)