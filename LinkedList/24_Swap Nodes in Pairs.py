class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0,head)
        curr = dummy 
        while(curr and curr.next and curr.next.next):
            first = curr.next 
            second = curr.next.next
            third = curr.next.next.next

            first.next = third
            second.next = first
            curr.next = second

            curr = curr.next.next


        return dummy.next
            