# https://leetcode.com/problems/combination-sum-ii/

class Solution: # T: 63.25% M: 25.10%%
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        def backtracking(i, subs, sum_):
            if i == len(candidates): 
                return None
            
            num = candidates[i]
            sum_num = sum_ + num
            if  sum_num == target:
                result.append(subs + [num])
                return None
            elif sum_num < target:
                backtracking(i + 1, subs + [num], sum_num)

            while i + 1 < len(candidates) and candidates[i + 1] == num:
                i += 1
            backtracking(i + 1, subs, sum_)
            
        backtracking(0, [], 0)
        return result