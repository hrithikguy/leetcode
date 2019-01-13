# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        unival = root.val
        
        stack = [root]
        while len(stack) > 0:
            cur = stack.pop()
            if cur != None:
                if cur.val != unival:
                    return False
                stack.append(cur.left)
                stack.append(cur.right)
            
        return True
