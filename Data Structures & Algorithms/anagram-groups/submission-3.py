#revision 1: dated 16 June, 2026

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        strToCounterMap = defaultdict(list)
        
        for str in strs:
            counterStr = [0] * 26

            for char in str:
                counterStr[ord(char)-ord('a')] += 1

            strToCounterMap[tuple(counterStr)].append(str)
        print(list((strToCounterMap).values()))

        return list((strToCounterMap).values())