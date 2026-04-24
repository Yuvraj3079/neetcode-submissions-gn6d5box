class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[1], nums[0])
        
        def robbery(arr):
            print(arr)
            if len(arr) == 1:
                return arr[0]
            
            dp = [0] * (len(arr))

            dp[0] = arr[0]
            dp[1] = max(arr[1], arr[0])
            #print(dp)
            for i in range(2, len(arr)):
                #print(i, arr[i])
                dp[i] = max(dp[i-1], dp[i-2]+ arr[i])
            print(dp)
            return dp[-1]

        n = len(nums) 
        #case1: excluding the last element
        print("Rob 1")
        rob1 = robbery(nums[1:])
        print("Rob 2")
        rob2 = robbery(nums[:-1])

        
        return max(rob1, rob2)

        