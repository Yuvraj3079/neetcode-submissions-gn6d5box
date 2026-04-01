class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        result = 0
        while right > left:
            temp = (right - left) * min(heights[left],heights[right])

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            result = max(temp,result)
        return result