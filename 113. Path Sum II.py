# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        res = []

        def backtrack(node, path, rem):
            if not node:
                return

            path.append(node.val)
            rem -= node.val

            if not node.left and not node.right and rem == 0:
                res.append(path[:])

            backtrack(node.left, path, rem)
            backtrack(node.right, path, rem)
            path.pop()

        backtrack(root, path, targetSum)
        return res
