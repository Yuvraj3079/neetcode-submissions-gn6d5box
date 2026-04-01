class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        #candidates = list(set(candidates))
        #sort array, so that we can skip the duplicates
        candidates.sort()
        def backtrack(start, path, currenSum):

            if currenSum == target:
                res.append(path[:])
                return
            if currenSum > target:
                return 
            for i in range(start, len(candidates)):
                #skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path, currenSum + candidates[i])
                path.pop()
            
        backtrack(0,[], 0)
        return res