class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = collections.deque()
        res = []
        for r in range(len(nums)):
            #popping elements that are smaller than nums[i]
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            #popping elements that are outside of the window k
            if q[0] < r + 1 - k:
                q.popleft()
            # r+1 because r started from 0 not 1
            if (r+1) >= k:
                res.append(nums[q[0]])

        return res