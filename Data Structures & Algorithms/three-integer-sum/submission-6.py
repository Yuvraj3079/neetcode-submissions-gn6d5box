class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        print(sorted_nums)

        result = []
        length = len(nums)
        for i in range(length):
            if sorted_nums[i] > 0:
                break
            left, right = i+1, len(nums) - 1

            #to skip the duplicates
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                print(i)
                continue
            else:
                while right > left:
                    sum = (sorted_nums[left] + sorted_nums[right]+sorted_nums[i])
                    #print(f'i: {i} left: {left} right:{right}')print(f'sum; {sum}')

                    if sum == 0:
                        result.append([sorted_nums[left], sorted_nums[right], sorted_nums[i]])

                        #skip duplicates
                        while left < right and sorted_nums[left]==sorted_nums[left+1]:
                            left +=1
                        while left < right and sorted_nums[right]==sorted_nums[right-1]:
                            right -= 1
                        #move both pointer after finding a triplet
                        left += 1
                        right -= 1
                        print(f'result: {left,right, i}')

                    elif sum < 0:
                        left += 1
                    else:
                        right -= 1



        return result