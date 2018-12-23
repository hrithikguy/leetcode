import collections

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #0 neither neighboor
        #1 down neighboor
        #2 up neighboor
        #3 both
        
        adj = collections.defaultdict(list)
        
        
        elems = set()
        best = 0
        
        for i in nums:
            elems.add(i)
            if i-1 in elems:
                adj[i].append(i-1)
                adj[i-1].append(i)
            if i+1 in elems:
                adj[i].append(i+1)
                adj[i+1].append(i)
             
        visited = set()
        max_size = 0
        for i in elems:
            if i in visited:
                continue
            cur_size = 0
            stack = [i]
            visited.add(i)
            while len(stack) > 0:
                cur = stack.pop()
                visited.add(cur)
                cur_size += 1
                for nei in adj[cur]:
                    if nei not in visited:
                        visited.add(nei)
                        stack.append(nei)
            max_size = max(max_size, cur_size)

        print max_size
        return max_size
        
            
            
