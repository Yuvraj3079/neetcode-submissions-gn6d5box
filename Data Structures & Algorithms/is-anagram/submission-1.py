class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = Counter(s)
        hashmapT = Counter(t)

        if hashmapS == hashmapT:
            return True
        else:
            return False
            