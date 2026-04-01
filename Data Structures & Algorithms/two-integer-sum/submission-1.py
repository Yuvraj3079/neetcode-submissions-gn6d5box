class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            #creating a key,value pair; key = index value
        preMap ={}

        #sorted_d = sorted(d.items(), key = lambda x:x[1])  sorted_d = dict(sorted_d)   print(d) print(sorted_d)

        for i,n in enumerate(nums):
            diff = target - n
            if diff in preMap:
                return [preMap[diff], i]
            preMap[n] = i
            #print(preMap)