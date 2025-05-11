class Solution:
    def permute(self, nums):

        res = []
        
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(path)
                path.pop()
            
        backtrack([])
        return res

sol = Solution()

# Test 1
print(sol.permute([1, 2, 3]))
# Expected:
# [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

# Test 2
print(sol.permute([0, 1]))
# Expected:
# [[0,1], [1,0]]

# Test 3
print(sol.permute([1]))
# Expected:
# [[1]]
