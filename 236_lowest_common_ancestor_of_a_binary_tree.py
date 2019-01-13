# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    result = None
    
    def count_descendants(self, root, p, q):
        output = 0
        
        if root == None:
            return 0
        
        if root == p or root == q:
            output += 1
            
        output += self.count_descendants(root.left, p, q) + self.count_descendants( root.right, p, q)
        
        if output == 2:
            self.result = root
            return 0
        
        return output
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        self.count_descendants(root, p, q)
        
        return self.result
        
        
