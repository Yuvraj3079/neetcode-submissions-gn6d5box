#Nov 20
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        sortedNums = list(sorted(set(nums)))
        longestS, count = 0, 1
        #print(sortedNums)
        for i in range(len(sortedNums)-1):
            
            if (abs(sortedNums[i+1] - sortedNums[i]) == 1):
                print(f"i: {longestS}")
                count += 1
            else:
                
                longestS = max(longestS, count)
                count = 1
                print(f"e: {longestS}, {count}")

        
        return max(longestS, count)