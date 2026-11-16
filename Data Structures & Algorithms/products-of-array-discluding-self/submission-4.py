#dated 16 Nov
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prev, after = [1] * n, [1] * n

        i = 1
        while i < n:
            prev[i] = prev[i-1] * nums[i-1]
            i += 1
        #print(prev)
        i = n - 2
        while i >= 0:
            after[i] = after[i+1] * nums[i+1]
            i -= 1
        #print(after)
        res = []
        i = 0
        while i < n:
            res.append(prev[i] * after[i])
            i += 1
        return res
