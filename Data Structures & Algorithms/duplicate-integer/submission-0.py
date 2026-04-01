class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkList = defaultdict(int)
        for num in nums:
            checkList[num] += 1
            if(checkList[num]>1):
                return True
        return False