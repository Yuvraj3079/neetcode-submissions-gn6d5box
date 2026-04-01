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
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        #create a used array to keep track of what elements have been used
        used = [False] * len(nums)
        def backtrack(start, path):
            #goal
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):

                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(i + 1, path)
                    path.pop()
                    used[i] = False

        
        backtrack(0,[])
        return res