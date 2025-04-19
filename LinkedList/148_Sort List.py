class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

class Solution:
    def half(self,yoo):
        slow = yoo
        fast = yoo
        
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            
        return slow
            
    def sortedd(self,head1,head2):
        fresh = ListNode(0)
        curr = fresh
        while(head1 and head2):
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next

            curr = curr.next
        
        if head2:
            curr.next = head2
        elif head1:
            curr.next = head1
        
        return fresh.next
            
    def sortList(self, head):
        
        if head.next is None:
            return head
        
        mid = self.half(head)
        nextt = self.sortList(mid.next)
        mid.next = None
        
        left = self.sortList(head)
        
        
        
        return self.sortedd(left,nextt)
        

        
        
node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)
node5 = ListNode(9)

# Linking nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5      

a = Solution()

res = a.sortList(node1)
print_linked_list(res)