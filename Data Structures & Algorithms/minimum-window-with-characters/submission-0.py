class Solution:
    def minWindow(self, s: str, t: str) -> str:
            if len(t) > len(s) or t == "":
                return ""

            countT, window = {}, {}

            #Count of char in String t
            for char in t:
                countT[char] = 1 + countT.get(char, 0)
            left = 0
            have, need = 0, len(countT)
            res, resultLength = [-1,-1], float('inf')

            for right in range(len(s)):
                char = s[right]
                #adding right to window
                window[char] = 1 + window.get(char,0)
                #check if we have the needed count
                if char in countT and window[char] == countT[char]:
                    have += 1
                # Shrinking the window till it meets the condition
                while have == need:
                    #update window
                    if (right - left + 1) < resultLength:
                        res = [left, right]
                        resultLength = right - left + 1
                    #pop from the left
                    window[s[left]] -= 1
                    #check
                    if s[left] in countT and window[s[left]] < countT[s[left]]:
                        have -= 1
                    left += 1

            left, right = res

            if resultLength != float('inf'):
                return s[left: right + 1]
            else:
                return ""
