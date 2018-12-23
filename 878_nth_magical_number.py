class Solution(object):
    def gcd(self, a, b):
        if a % b == 0 or b % a == 0:
            return min(a,b)
        if a== 1 or b==1:
            return 1
        if a== b:
            return a
        if a > b:
            c = a/b
            return self.gcd(a - c * b, b)
        if a <= b:
            c = b/a
            return self.gcd(a, b- c *a)
        
    
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        print self.gcd(A,B)
        C = A * B / self.gcd(A,B)
        print "LCM", C
        A = float(A)
        B = float(B)
        C = float(C)
        out = float(N * A * B * C)/float(B * C + A * C- A*B)
        print out
        newout = int(out) + int(A) + int(B)
        
        frac = 1.0/A + 1.0/B - 1.0/C
        print frac
        while newout/int(A) + newout/int(B) - newout/int(C) >= N:
            newout -= 1
            
        return (newout + 1) % 1000000007
        
        
        if out % 1 > 0:
            return int(out) + 1
        else:
            return int(out)
