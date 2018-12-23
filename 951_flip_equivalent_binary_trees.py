# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == None and root2 == None:
            return True
        if root1 == None and root2 != None:
            return False
        if root1 != None and root2 == None:
            return False
        
        if root1.val != root2.val:
            return False
        
        
        Achildren = []
        Bchildren = []
        
        if root1.left == None:
            Achildren.append(None)
        else:
            Achildren.append(root1.left.val)
        
        if root1.right == None:
            Achildren.append(None)
        else:
            Achildren.append(root1.right.val)
        
        
        if root2.left == None:
            Bchildren.append(None)
        else:
            Bchildren.append(root2.left.val)
        
        if root2.right == None:
            Bchildren.append(None)
        else:
            Bchildren.append(root2.right.val)
        
        if Achildren == Bchildren:
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        
        else:
            t = Achildren[0]
            Achildren[0] = Achildren[1]
            Achildren[1] = t
            if Achildren == Bchildren:
                return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
            else:
                return False
            
        
