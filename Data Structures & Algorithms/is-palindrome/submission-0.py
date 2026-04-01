class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0

        str_mod = re.sub(r'[^a-z0-9A-Z]','',s).lower()

        print(str_mod)

        end = len(str_mod) - 1
        while end >= start:
            if str_mod[start] == str_mod[end]:
                start += 1
                end -= 1
            else:
                return False
        return True