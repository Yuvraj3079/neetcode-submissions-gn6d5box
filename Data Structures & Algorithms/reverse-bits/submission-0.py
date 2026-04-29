class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            #see if the ith bit is 1 or not
            bit = (n >>i) & 1
            print(bit)
            res = res | (bit << (31-i))
            print("res", res)
        return res
                
        