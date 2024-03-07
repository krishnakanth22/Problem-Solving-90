# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return None
        List=[]
        def helper (node):
            if node:
                helper(node.left)
                List.append(node.val)
                helper(node.right)
        helper(root)
        return List
