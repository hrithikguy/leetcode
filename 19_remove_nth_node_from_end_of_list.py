# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        output = head
        p1 = head
        p2 = head
        
        for i in range(n):
            p1 = p1.next
            
        if p1 == None:
            return head.next
            
        while (p1 != None):
            p1 = p1.next
            if p1 == None:
                p2.next = p2.next.next
                break
            p2 = p2.next
            
        return output
