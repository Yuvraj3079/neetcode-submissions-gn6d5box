class Solution:
    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def backtrack(i):

            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):

                substring = s[i: j+1]

                if self.isPalindrome(substring):
                    part.append(substring)
                    backtrack(j+1)
                    part.pop()
        backtrack(0)
        return res
        