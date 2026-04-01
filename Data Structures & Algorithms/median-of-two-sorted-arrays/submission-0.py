class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2

        merged.sort()
        l, r = 0, len(merged)
        mid = l + (r-l)//2
        if r % 2 == 0:
            return (merged[mid-1]+merged[mid])/2
        else:
            return merged[mid]