# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if head is None or head.next is None:
            return head
        dummy =  ListNode(0,head)
        length = 0
        curr = dummy
        
        while(length + 1 != left):
            length += 1
            curr = curr.next
        
        
        next = curr.next
        for _ in range(0,right-left):
            temp = next.next
            next.next = next.next.next
            prev_next = curr.next
            temp.next = prev_next
            curr.next = temp
    
            
        return dummy.next