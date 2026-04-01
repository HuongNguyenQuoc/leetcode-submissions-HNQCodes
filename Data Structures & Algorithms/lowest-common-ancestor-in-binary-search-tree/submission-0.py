# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        target = root
        while target:
            if p.val < target.val and q.val < target.val:
                target = target.left
            elif p.val > target.val and q.val > target.val:
                target = target.right
            else:
                return target

        return None