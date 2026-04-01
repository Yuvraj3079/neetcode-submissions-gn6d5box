class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        length = 0
        while i < len(s):
            #get length of the string
            j = i
            while j<len(s) and s[j] != "#":
                j+=1

            length = int(s[i:j])
            print(length)
            start = j+1
            end = start + length
            #splice string from index start to index end
            decoded.append(s[start:end])
            i = end

        #print(decoded)
        return decoded
