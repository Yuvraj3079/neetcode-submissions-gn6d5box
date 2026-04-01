class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = defaultdict(int)
        dicT = defaultdict(int)
        if(len(s)!=len(t)):
            return False

        for i in s:
            dicS[i] += 1

        for i in t:
            dicT[i] += 1

        if (dicS == dicT):
            return True
        else:
            return False