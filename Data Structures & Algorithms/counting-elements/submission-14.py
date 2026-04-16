class Solution:
    def countElements(self, arr: List[int]) -> int:
        
        count = Counter(arr)

        x = 0

        for num in arr:
            if count[num + 1] > 0:
                x += 1
        return x