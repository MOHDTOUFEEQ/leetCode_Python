class Solution:
    def insertGreatestCommonDivisors(self, head):
        if head is None or head.next is None:
            return head
        
        curr = head
        
        while(curr and curr.next):
            val = gcd(curr.val,curr.next.val)
            newNode = ListNode(val)
            temp = curr.next
            curr.next = newNode
            newNode.next = temp
            curr = curr.next.next

        return head