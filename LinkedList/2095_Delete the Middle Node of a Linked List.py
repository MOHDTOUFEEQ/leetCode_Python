class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        if head is None or head.next is None:
            return None
        dummy =  ListNode(0,head)
        slow = head
        fast = head
        curr = dummy
        while(fast.next and fast.next.next ):
            slow = slow.next
            curr = curr.next
            fast = fast.next.next
        
        if fast.next:
            slow.next = slow.next.next
        else:
            curr.next = curr.next.next
        
        return dummy.next