class Solution:
    '''
    what i am thinking is creating 2 arrays:
    array1: store product before ith position
    array2: store product after ith position

    later on, we multiply both arrays 
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        productBeforeI, productAfterI = [1] * len(nums), [1] * len(nums)

        for i in range(len(nums)-1):
            productBeforeI[i+1] = productBeforeI[i] * nums[i]
        
        print(productBeforeI)
        temp = 1
        i = len(nums) - 1
        while i > 0:

            temp = temp * nums[i]
            productAfterI[i]= temp
            i -= 1
        #print(productAfterI)
        productAfterI[1:len(nums)] =  productAfterI[1:len(nums)][::-1]
        #print(productAfterI)
        
        productAfterI.reverse()
        result = []
        for i in range(len(nums)):
            result.append (productAfterI[i] * productBeforeI[i])
        
        return result


