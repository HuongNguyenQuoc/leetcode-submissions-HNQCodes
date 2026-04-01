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
            curr = stack.pop()
            if not curr:
                res.append("null")
                continue
            res.append(str(curr.val))
            stack.append(curr.right)
            stack.append(curr.left)
        return ",".join(res)

        

    def deserialize(self, data):
        target = data.split(",")
        self.i = 0
        def dfs():
            if target[self.i] == "null":
                self.i += 1
                return None
            node = TreeNode(int(target[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))