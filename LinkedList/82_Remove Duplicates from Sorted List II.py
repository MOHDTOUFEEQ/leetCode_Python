class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        dummy = ListNode(0,head)
        prev = dummy
        curr = prev.next

        while(curr and curr.next ):
            nextNode = curr.next
            if(curr and curr.val == nextNode.val):
                while(nextNode and curr.val == nextNode.val):
                    nextNode = nextNode.next

                prev.next = nextNode
                curr = nextNode
            else:
                prev = curr
                curr = curr.next

        return dummy.next

                