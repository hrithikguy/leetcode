# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getDepth(self, root):
        if root == None:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))
    
    
    
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        
        if leftDepth == rightDepth:
            return root
        
        if leftDepth > rightDepth:
            return self.subtreeWithAllDeepest(root.left)
        
        if rightDepth > leftDepth:
            return self.subtreeWithAllDeepest(root.right)
            
        
