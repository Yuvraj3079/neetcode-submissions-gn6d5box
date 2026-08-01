class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        rather than storing prefix and postfix array, we can compute the result in 2 passes
        first pass: stores left product 
        2nd pass: multiplies right product on the fly
        '''

        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1,-1,-1):
            result[i] *= postfix
            postfix *= nums[i]
        return result


