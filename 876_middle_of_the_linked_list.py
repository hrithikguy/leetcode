# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        p1count = 1
        p2count = 1
        while True:
            print p1count, p2count
            p1 = p1.next
            if p1 == None:
                return p2
                # print "b1"
                # if p1count % 2 == 0:
                #     if p2count == p1count/2:
                #         p2 = p2.next
                #     return p2
                # else:
                #     return p2
            p1count+=1
            p1 = p1.next
            if p1 == None:
                # print p1count, p2count
                # return p2
                print "b2"
                print p1count, p2count
                if p1count % 2 == 0:
                    if p2count == p1count/2:
                        p2 = p2.next
                    return p2
                else:
                    return p2
            p1count+=1
            p2 = p2.next
            p2count += 1
            
        return p2
