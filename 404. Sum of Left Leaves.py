# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0  # Stores the sum of left leaves

        def backtrack(node, is_left):
            if not node:
                return
            
            if is_left and not node.left and not node.right:
                self.total += node.val
            
            backtrack(node.left, True)
            backtrack(node.right, False)
        
        backtrack(root, False)
        return self.total
