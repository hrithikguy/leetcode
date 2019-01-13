class Solution(object):
    def isPalindrome(self, s):
        p1 = 0
        p2 = len(s) - 1
        
        while (p1 <= p2):
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
            
        return True
            
            
        # return s == s[::-1]
        # if len(s) < 2:
        #     return True
        # if s[0] != s[-1]:
        #     return False
        # else:
        #     return self.isPalindrome(s[1:-1])
    
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1 = 0
        p2 = len(s)-1
        
        while (p1 <= p2):
            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return self.isPalindrome(s[p1:p2]) or self.isPalindrome(s[p1+1:p2+1])
            
        return True
                
        
#         if len(s) < 3:
#             return True
        
#         else:
#             if s[0] == s[-1]:
#                 return self.validPalindrome(s[1:-1])
#             else:
#                 return self.isPalindrome(s[1:]) or self.isPalindrome(s[:-1])
