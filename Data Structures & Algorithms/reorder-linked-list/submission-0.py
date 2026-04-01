# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        #Reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        #Merge two halfs
        first, second = head, prev
        while second:
            target = first.next
            first.next = second
            first = second
            second = target
        
        

        

        
