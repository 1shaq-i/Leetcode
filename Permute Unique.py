class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        used = {}
        for num in nums:
            used[num] = used.get(num, 0) + 1  # frequency count

        def backtrack(path, used_map):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for num in used:
                if used_map[num] > 0:
                    # choose
                    path.append(num)
                    used_map[num] -= 1

                    # explore
                    backtrack(path, used_map)

                    # un-choose
                    path.pop()
                    used_map[num] += 1

        backtrack([], used.copy())
        return res
