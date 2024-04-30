# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 1)])
        while q:
            cur_node, level = q.popleft()
            if not cur_node.left and not cur_node.right:
                return level
            if cur_node.left:
                q.append((cur_node.left, level+1))
            if cur_node.right:
                q.append((cur_node.right, level +1))
