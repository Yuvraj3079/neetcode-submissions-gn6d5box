class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #if len(s1) is greater than len of s2, then there's no point of checking
        if len(s1) > len(s2):
            return False

        window = len(s1)
        freq_list_s1, freq_list_s2 = [0] * 26, [0] * 26
        #creating frequency list for String s1
        for i in range(window):
            freq_list_s1[ord(s1[i]) - ord('a')] += 1
        print(freq_list_s1)

        #creating inital frequency array for s2
        for i in range(window):
            freq_list_s2[ord(s2[i]) - ord('a')] += 1
        
        if freq_list_s1 == freq_list_s2:
                return True

        for right in range(window, len(s2)):
            #add a char (right)
            freq_list_s2[ord(s2[right]) - ord('a')] += 1
            #remving left char (left = right - window)
            freq_list_s2[ord(s2[right - window]) - ord('a')] -= 1

            print(f'S2 Frequency list: {freq_list_s2}')
            if freq_list_s1 == freq_list_s2:
                return True

        return False

 