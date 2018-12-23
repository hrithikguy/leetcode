class Solution(object):
    def get_permutations(self, A):
        # print A
        if len(A) == 1:
            return [A]
        
        else:
            out = []
            for i in range(len(A)):
                B = []
                for k in A:
                    B.append(k)
                prefix = B[i]
                del B[i]
                suffixes = self.get_permutations(B)
                for j in suffixes:
                    cur = [prefix] + j
                    out.append(cur)
                    
            return out
