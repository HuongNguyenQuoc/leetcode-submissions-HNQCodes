# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        stack = [(p, q)]

        while stack:
            a, b = stack.pop()

            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False 

            stack.append((a.left, b.left))
            stack.append((a.right, b.right))
        return True