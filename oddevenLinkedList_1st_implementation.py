class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else: 
            final_connection = head.next
            odd = head
            even = head.next
            while True:
                if (even.next is not None):
                    odd.next = even.next  
                else: 
                    odd.next = final_connection
                    even.next = None
                    return head
                if (even.next.next is not None):
                    even.next = even.next.next
                else:
                    even.next.next = final_connection
                    even.next = None
                    return head
 
                odd = odd.next
                even = even.next
