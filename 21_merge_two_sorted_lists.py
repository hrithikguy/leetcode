# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        p1 = l1
        p2 = l2
        if p1 == None:
            return p2
        if p2 == None:
            return p1
        if p1.val < p2.val:
            head = p1
            p1 = p1.next
        else:
            head = p2
            p2 = p2.next
            
            
        cur = head
        while (p1 != None and p2 != None):
            if p1.val < p2.val:
                cur.next = p1
                cur = cur.next
                p1 = p1.next
            else:
                cur.next = p2
                cur = cur.next
                p2 = p2.next
                
            
        while p1 != None:
            cur.next = p1
            cur = cur.next
            p1 = p1.next
            
        while p2 != None:
            cur.next = p2
            cur = cur.next
            p2 = p2.next
            
        return head
            
        
        
        
