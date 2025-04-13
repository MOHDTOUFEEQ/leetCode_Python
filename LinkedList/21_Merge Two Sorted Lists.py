# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        curr = list1
        curr1 = list2
        dummy = ListNode(0)
        res = dummy
        while(curr1 and curr):
            if curr1.val <= curr.val:
                node = ListNode(curr1.val)
                res.next = node
                curr1 = curr1.next
            else:
                node = ListNode(curr.val)
                res.next = node
                curr = curr.next

            res = res.next
        
        if curr:
            res.next = curr
        elif curr1:
            res.next = curr1
            


        return dummy.next
