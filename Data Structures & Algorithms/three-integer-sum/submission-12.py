class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = {}
        nums = sorted(nums)
        for i in range(len(nums)):
            
            nAtindexI = nums[i]

            left, right = i+1, len(nums) - 1
            
            while left < right:

                sum = nAtindexI + nums[left] + nums[right]
                #print(nAtindexI, nums[left], nums[right])
                if sum == 0:
                    #if [nAtindexI, nums[left], nums[right]] not in result:
                    result[(nAtindexI, nums[left], nums[right])] = 1
                if sum > 0:
                    right -= 1
                else:
                    left += 1
            

        return list(result)