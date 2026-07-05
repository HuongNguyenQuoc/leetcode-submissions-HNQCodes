# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if not root:
      return True

    def dfs(node):
      if not node:
        return 0

      lst = dfs(node.left)
      if lst == -1:
        return -1

      rst = dfs(node.right)
      if rst == -1:
        return -1

      if abs(lst - rst) > 1:
        return -1

      return 1 + max(lst, rst)

    return dfs(root) != -1
