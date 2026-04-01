# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        '''if not root:
            return True
        q = deque([(root, float("-inf"), float("inf"))])
        while q:
            node, left, right = q.popleft()
            if not left < node.val < right:
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))
        return True'''


        if not root:
            return True
        q = deque([(root, float('-inf'), float('inf'))])
        while q:
            cur, lsb, rsb = q.popleft()
            if lsb >= cur.val or rsb <= cur.val:
                return False
            if cur.left is not None:
                q.append((cur.left, lsb, cur.val))
            if cur.right is not None:
                q.append((cur.right, cur.val, rsb))
        return True