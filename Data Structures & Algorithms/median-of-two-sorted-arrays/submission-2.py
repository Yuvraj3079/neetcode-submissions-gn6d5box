class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2
        left, right = 0, m 

        while left <= right:

            partition1 = left + (right - left)//2
            partition2 = half - partition1

            nums1LeftMax = nums1[partition1 - 1] if partition1 > 0 else float("-inf")
            nums1RightMin = nums1[partition1] if partition1 < m else float("inf")
            nums2LeftMax = nums2[partition2 - 1] if partition2 > 0 else float("-inf")
            nums2RightMin = nums2[partition2] if partition2 < n else float("inf")
            print(f'left: {left}, right: {right}')
            print(f'nums1')
            print(nums1LeftMax, nums1RightMin)
            print(f'nums2')
            print(nums2LeftMax, nums2RightMin)
            print(f'{nums1LeftMax} <= {nums2RightMin} and {nums2LeftMax} <= {nums2LeftMax} ')
            
            if nums1LeftMax <= nums2RightMin and nums2LeftMax <= nums1RightMin:
                print("return")
                if total%2 == 1:
                    return max(nums1LeftMax, nums2LeftMax)
                else:
                    return (min(nums1RightMin, nums2RightMin) + max(nums1LeftMax, nums2LeftMax))/2
            elif nums1LeftMax > nums2RightMin:
                right = partition1 - 1
            else:
                left = partition1 + 1
            
        return 0
            