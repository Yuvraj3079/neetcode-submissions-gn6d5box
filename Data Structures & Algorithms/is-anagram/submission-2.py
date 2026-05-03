class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = Counter(s)
        counterT = Counter(t)

        if counterS == counterT:
            return True
        else:
            return False