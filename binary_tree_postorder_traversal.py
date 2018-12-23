# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, output):
    
        if root == None:
            return
        
        self.helper(root.left, output)
        self.helper(root.right, output)
        output.append(root.val)
        
        
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        output = []
        self.helper(root, output)
        
        return output
        
