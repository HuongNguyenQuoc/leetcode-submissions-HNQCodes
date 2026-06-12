# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        target = tail = head
        cnt = 0

        while tail.next is not None:
            tail = tail.next
        
        while target:
            if cnt == index: 
                return True
            cnt += 1
            target = target.next 
        return False