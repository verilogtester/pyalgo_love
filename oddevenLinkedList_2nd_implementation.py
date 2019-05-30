class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #create two dummy nodes [Assuming 0 in the list not present, otherwise take other value]
        d1 = odd  = ListNode(0)
        d2 = even = ListNode(0)
        
        while head:
            odd.next  = head #points to 1
            even.next = head.next #points to 2
            
            # pointer shift by 1
            odd  = odd.next
            even = even.next
            
            if even.next.next is not None:
                head = head.next.next
            else:
                head = None
        odd.next = d2.next
        return d1.next
