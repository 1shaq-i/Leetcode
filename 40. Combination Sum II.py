class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, combo, total):

            if total == target:
                res.append(combo[:])
            
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # skip duplicate choices at the same level
                combo.append(candidates[i])
                backtrack(i + 1, combo, candidates[i] + total)
                combo.pop()
        
        backtrack(0, [], 0)

        return res
