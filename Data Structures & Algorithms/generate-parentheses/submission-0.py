'''
def backtrack(choices, path, result):
    if goal_reached:
        result.append(path[:])
        return
    
    for choice in available_choices:
        # Prune if invalid (optional)
        if is_valid(choice):
            path.append(choice)           # Make choice
            backtrack(updated_choices, path, result)  # Explore
            path.pop()                    # Undo choice
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open, closed, path):

            if open == closed == n:
                res.append(path[:])
                return
            
            if open < n:
                path += '('
                backtrack(open + 1, closed, path)
                path = path[:-1]
            
            if closed < open:
                path+=')'
                backtrack(open, closed + 1, path)
                path = path[:-1]
        
        backtrack(0,0,"")
        print(res)
        return res


