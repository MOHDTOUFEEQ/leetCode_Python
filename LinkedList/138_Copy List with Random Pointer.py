class Solution:
    def copyRandomList(self, head):
        obj = {}

        curr = head

        while(curr):
            obj[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        for i in obj.values():
            i.next = obj.get(curr.next, None)
            i.random = obj.get(curr.random, None) 
            curr = curr.next


        return obj[head]