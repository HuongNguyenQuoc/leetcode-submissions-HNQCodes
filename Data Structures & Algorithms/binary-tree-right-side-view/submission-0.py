# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []
        while q:
            level = len(q)
            for i in range(level):
                node = q.popleft()
                if i == 0: #Node đầu tiên của level
                    res.append(node.val)
                #Thêm phải trước, trái sau
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return res