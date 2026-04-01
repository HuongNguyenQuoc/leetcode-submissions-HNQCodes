# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None: return None
        l, r = head, head
        prev = None
        for i in range(n):
            r = r.next
        while r:
            prev = l
            l = l.next
            r = r.next
        if prev is None:
            head = head.next
        else:
            prev.next = l.next
        return head
