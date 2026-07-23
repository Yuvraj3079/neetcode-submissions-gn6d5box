class Solution:

    def encode(self, strs: List[str]) -> str:

        separator = "$#"
        result = ""
        for s in strs:
#Strings are immutable in py, so we need to convert it into a list then join them
            s_list = list(s)
            
            result += s + separator
        print(result)
        return result
            

    def decode(self, s: str) -> List[str]:
        encodedString = list(s)
        st = ""
        separator = "$#"
        result = s.split(separator)
        result.pop(-1)

        


        return result
