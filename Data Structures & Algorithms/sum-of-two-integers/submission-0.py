class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry
#~(a ^ 0xFFFFFFFF) is typically used to simulate 32-bit signed integer behavior
# and -(x + 1)
        return a if a <= max_int else ~(a ^ mask)