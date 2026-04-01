"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        HashMap = {None : None}

        cur = head
        while cur:
            tmp = Node(cur.val)
            HashMap[cur] = tmp
            cur = cur.next
        
        cur = head
        while cur:
            tmp = HashMap[cur]
            tmp.next = HashMap[cur.next]
            tmp.random = HashMap[cur.random]
            cur = cur.next
        
        return HashMap[head]