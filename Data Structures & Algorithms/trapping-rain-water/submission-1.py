class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL,maxR = [0]*n, [0]*n
        maxL[0], maxR[n-1] = height[0], height[n-1]
        for i in range(1,n):
            maxL[i] = max(maxL[i-1], height[i])
        #print(maxL)
        
        for i in range(n-2, -1, -1):
            maxR[i] = max(maxR[i+1],height[i])
        #print(maxR)

        minLR = []
        for i in range(n):
            minLR.append(min(maxL[i],maxR[i]))
            #minLR[i] = min(maxL[i],maxR[i])
        total = 0
        for i in range(n):
            
            if (minLR[i] - height[i])>0:
                total += minLR[i] - height[i]
        return total