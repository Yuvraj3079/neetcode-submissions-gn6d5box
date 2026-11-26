class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL,maxR = [0]*n, [0]*n
        #initialize the first element of maxL and last element of maxR
        maxL[0], maxR[n-1] = height[0], height[n-1]
        for i in range(1,n):
            maxL[i] = max(maxL[i-1], height[i])
        #print(maxL)
        
        for i in range(n-2, -1, -1):
            maxR[i] = max(maxR[i+1],height[i])
        #print(maxR)

        total = 0
        for i in range(n):
            total += min(maxL[i],maxR[i]) - height[i]
        return total