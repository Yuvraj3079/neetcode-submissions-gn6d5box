class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {'2' : 'abc',
                    '3' : 'def',
                    '4' : 'ghi',
                    '5' : 'jkl',
                    '6' : 'mno',
                    '7' : 'pqrs',
                    '8' : 'tuv',
                    '9' : 'wxyz'}
        
        res = []

        def backtrack(index, path):

            if index == len(digits):
                res.append(''.join(path))
                return
            
            digit = digits[index]
            letters = digitMap[digit]
            print(path)
            for letter in letters:
                path.append(letter)
                backtrack(index +1 , path)
                path.pop()
        
        backtrack(0,[])

        return res

            
