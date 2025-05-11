class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()  # Step 1: Sort to bring duplicates together

        def backtrack(start, path):
            res.append(path[:])  # Always add current subset

            for i in range(start, len(nums)):
                # Step 2: Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res



sol = Solution() 

# Test Case 1: No duplicates
print(sol.subsetsWithDup([1, 2]))  
# Expected: [[], [1], [2], [1, 2]]

# Test Case 2: With duplicates
print(sol.subsetsWithDup([1, 2, 2]))
# Expected: [[], [1], [2], [1,2], [2,2], [1,2,2]]

# Test Case 3: All duplicates
print(sol.subsetsWithDup([2, 2, 2]))
# Expected: [[], [2], [2,2], [2,2,2]]

# Test Case 4: Empty list
print(sol.subsetsWithDup([]))
# Expected: [[]]
