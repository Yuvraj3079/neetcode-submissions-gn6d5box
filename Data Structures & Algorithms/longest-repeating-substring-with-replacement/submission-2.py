class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0,0
        max_freq,result = 0,0
        max_freq_list = Counter()
        for right in range(len(s)):
            max_freq_list[s[right]] += 1

            max_freq = max(max_freq,max_freq_list[s[right]])

            window = right - left + 1
            if (window - max_freq) <= k:
                result = max(result,window)
            else:
                #removes s[left] from Counter list i.e. max_freq_list
                #print(max_freq_list)
                max_freq_list[s[left]] -= 1
                #print(f'after removing {s[left]} : {max_freq_list}')
                left += 1

        return result