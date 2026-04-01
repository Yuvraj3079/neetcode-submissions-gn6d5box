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
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(start, path, currentSum):
            #Goal 
            if currentSum == target:
                res.append(path[:])
                return
            if currentSum > target:
                return
            
            for i in range(start, len(nums)):

                path.append(nums[i])
                backtrack(i, path, currentSum + nums[i])
                path.pop()
        
        backtrack(0,[], 0)
        return res
