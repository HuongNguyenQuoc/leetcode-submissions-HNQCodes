# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return "null"
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if not node:
                res.append("null")
                continue
            res.append(str(node.val))
            stack.append(node.right)
            stack.append(node.left)
        return ",".join(res)

    def deserialize(self, data):
        target = data.split(",")
        self.i = 0
        def dfs():
            if target[self.i] == "null":
                self.i += 1
                return None
            root = TreeNode(int(target[self.i]))
            self.i += 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))