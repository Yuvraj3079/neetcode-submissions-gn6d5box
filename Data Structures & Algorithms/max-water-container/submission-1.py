class Solution:

    '''
    we will have 2 pointers; one pointing at the left and another at the right

    move left pointer if heights[left] < heights[right]
    and vice versa
    '''
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1

        maxArea = 0

        while left < right:

            area = (right - left) * min(heights[left], heights[right])

            maxArea = max(area, maxArea)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxArea
        