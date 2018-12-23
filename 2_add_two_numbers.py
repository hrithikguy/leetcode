# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = ListNode(0)
        head = output
        carry = 0
        while l1 != None or l2 != None:
            if l1 != None and l2 != None:
                cur_val = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1 != None and l2 == None:
                cur_val = l1.val + carry
                l1 = l1.next
            elif l1 == None and l2 != None:
                cur_val = l2.val + carry
                l2 = l2.next
            carry = cur_val/10
            cur_val = cur_val % 10
            output.val = cur_val
            if l1 != None or l2 != None or carry > 0:
                next_output = ListNode(0)
                output.next = next_output
                output = output.next
        if carry > 0:
            output.val = carry
        return head
