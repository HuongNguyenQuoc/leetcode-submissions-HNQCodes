# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        def dfs(node):
            nonlocal cnt
            if not node:
                return None
            dfs(node.left)
            cnt -= 1
            if cnt == 0:
                return node.val
            dfs(node.right)
        
        dfs(root)
        return root.val