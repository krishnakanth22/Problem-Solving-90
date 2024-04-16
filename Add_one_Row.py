# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, current_depth):
            if not node:
                return None
            if current_depth == depth - 1:
                node.left = TreeNode(val, left=node.left)
                node.right = TreeNode(val, right=node.right)
            else:
                node.left = dfs(node.left, current_depth + 1)
                node.right = dfs(node.right, current_depth + 1)
            return node
        if depth == 1:
            new_root = TreeNode(val, left=root)
            return new_root
        
        return dfs(root, 1)
