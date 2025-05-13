# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(current_node):
            if not current_node:  # Base case: if node is None, return
                return
            res.append(current_node.val)  # Visit root
            traverse(current_node.left)   # Traverse left
            traverse(current_node.right)  # Traverse right

        traverse(root)  # Start traversal from the root
        return res
