#revision 1: dated 16 June, 2026
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counterS = Counter(s)
        counterT = Counter(t)

        if counterS == counterT:
            return True
        else:
            return False


        
        