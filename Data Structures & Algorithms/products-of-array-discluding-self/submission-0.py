class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        length = len(nums)
        leftProduct = [length]
        rightProduct = [length]


        leftProduct[0] = rightProduct[0] = 1
        i = 1
        temp = 1
        while i < length:
            temp = temp * nums[i-1]
            #print(f"temp at {i} = {temp}")
            leftProduct.append(temp)
            i += 1
        #print(leftProduct)
        temp = 1
        i = length - 1
        while i > 0:
            temp = temp * nums[i]
            #print(f"temp at {i} = {temp}")
            rightProduct.append(temp)
            i -= 1
        k = 0
        while k < length:
            result.append(leftProduct[k]*rightProduct[length-k-1])
            k += 1

        #print(rightProduct)
        return result 
        