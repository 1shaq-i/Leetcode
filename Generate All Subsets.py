class Solution:
    def GenerateAllSubsets(self, nums):
        res = []

        def backtrack(start, path):
            res.append(path[:])  # Add current subset

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)  # move forward
                path.pop()  # backtrack

        backtrack(0, [])
        return res
