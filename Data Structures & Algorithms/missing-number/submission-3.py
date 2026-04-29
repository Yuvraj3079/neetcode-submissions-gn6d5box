class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorNums = nums[0]
        xor = n
        for i in range(1,n):
            xorNums ^= nums[i]
            xor ^= i

        print(xorNums, xor)
        return (xor ^ xorNums)