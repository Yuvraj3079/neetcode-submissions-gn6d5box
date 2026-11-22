#Nov 21
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            #skip duplicates
            if nums[i] == nums[i-1] and i > 0:
                continue
            l, r = i + 1, n - 1

            while l < r:
                total = nums[i]+nums[l]+nums[r]

                if total == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    #skip duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return res

