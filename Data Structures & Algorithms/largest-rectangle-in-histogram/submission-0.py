class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        maxArea = 0

        for (i, h) in enumerate(heights):

            start = i

            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                maxArea = max(maxArea, (i - index) * height)
                start = index

            stack.append((start,h))

        #calculate area for remaining elements in stack print(stack)
        for i,h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)

        return maxArea        