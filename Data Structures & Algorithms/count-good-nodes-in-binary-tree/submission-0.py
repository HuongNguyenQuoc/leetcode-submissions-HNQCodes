# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([(root, float('-inf'))])
        ans = 0
        while q:
            node, cM = q.popleft()
            if node.val >= cM:
                ans += 1
            newMax = max(node.val, cM)
            if node.left:
                q.append((node.left, newMax))
            if node.right:
                q.append((node.right, newMax))
        return ans