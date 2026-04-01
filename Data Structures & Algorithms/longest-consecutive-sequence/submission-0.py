class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numsSet = set(nums)
        longest = 0

        for num in nums:
            #check if this is start of the sequence
            #number is the start if (num - 1) doesn't exist
            if (num - 1) not in numsSet:
                current = num
                current_length = 1
                
                #keep checking for consecutive numbers
                while (current + 1) in numsSet:

                    current_length += 1
                    current += 1

                longest = max(longest,current_length)

        return longest