# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        target = find = head

        while target and target.next:
            target = target.next.next
            find = find.next
            if target == find:
                return True
        return False