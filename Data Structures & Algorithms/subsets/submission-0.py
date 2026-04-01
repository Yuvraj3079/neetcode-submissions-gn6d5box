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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(start, path):
            #add current subset
            res.append(path[:]) #result.append(path.copy()) # copy() method

            for i in range(start, len(nums)):
                #making a choice
                path.append(nums[i])
                #exploring next choices, starting from i + 1 
                backtrack(i+1, path)
                #deleting the choice
                path.pop()

        backtrack(0, [])
        return res
