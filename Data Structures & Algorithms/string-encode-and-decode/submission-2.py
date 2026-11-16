#revision 1: dated 05 Nov, 2026
class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedS = ""
        for s in strs:
            encodedS += f"{len(s)}#{s}"
        #print(encodedS)
        return encodedS
        

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j+1: j+1+length])
            i = j+1+length

        #print(decoded)
        return decoded
