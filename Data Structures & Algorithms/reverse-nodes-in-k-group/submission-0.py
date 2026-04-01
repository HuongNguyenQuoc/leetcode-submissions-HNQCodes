# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head:
            return head
        
        dummy = ListNode(0, head)
        groupPrev = dummy

        def getKth(curr, k):
            #Return last node of group
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        while True:
            Kth = getKth(groupPrev, k)
            if Kth is None: #Nhóm mới không đủ k node hoặc Kth == None
                break
            
            groupNext = Kth.next
            prev = groupNext
            curr = groupPrev.next
            
            #Start reverse k nodes in linked list
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            #After reverse, reconnect the nodes to avoid splitting into 2 linked lists
            groupStart = groupPrev.next
            groupPrev.next = Kth
            groupPrev = groupStart
        
        return dummy.next

            