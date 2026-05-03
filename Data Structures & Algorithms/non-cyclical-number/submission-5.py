class Solution:
    def isHappy(self, n: int) -> bool:
        hash = set()

        def numberToDigit(n):
            print("function")
            if int(n/10) == 0:
                return n**2
            x = 0
            while n != 0:
                digit = n % 10
                n = int(n/10)
                x += digit**2
            
            return x
        
        result = numberToDigit(n)
        if result == 1:
            return True
        
        while result not in hash:
            
            if result == 1:
                return True
            hash.add(result)

            if int(result/10) != 0:
                result = numberToDigit(result)
                print(result)
            
        return False


        