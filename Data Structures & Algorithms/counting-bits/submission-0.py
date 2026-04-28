class Solution:
    def countBits(self, num: int) -> List[int]:
        def countN(n):
            count = 0

            while n > 0:
                if n & 1 == 1:
                    count += 1
                n = n >> 1
            return count
        res = []

        for i in range(num + 1):
            res.append(countN(i))
        
        return res