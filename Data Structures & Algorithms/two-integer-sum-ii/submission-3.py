class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        while end >= start:

            #print(f'start: {start} end:{end}')
            if (numbers[start] + numbers[end]) == target:
                #print(f'{numbers[start], numbers[end]}')
                return [start+1, end+1]

            if numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1
            #print(f'start: {start} end:{end}')
        