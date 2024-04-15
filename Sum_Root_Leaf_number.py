# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(curr,result):
            if not curr:
                return 0
            result=result*10 + curr.val
            if not curr.left and not curr.right :
                return result
            return dfs(curr.left, result) + dfs(curr.right, result)
        return dfs(root,0)
