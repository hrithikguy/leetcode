class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # value, index
        stack = []
        out = 0
        for i,j in enumerate(height):
            if len(stack) == 0 or j <= stack[-1][0]:
                stack.append((j, i))
            else:
                while len(stack) > 0:
                    cur = stack.pop()
                    for k in range(cur[1]+1, i):
                        out += min(cur[0], j) - height[k]
                        height[k] = min(cur[0], j)
                        
                    if cur[0] > j:
                        stack.append((cur[0], cur[1]))
                        break
                
                stack.append((j,i))
                
        return out
