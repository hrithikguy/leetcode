class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        visited = set()
        sizes = {0: 0}
        
        cur_component_index = 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited or grid[i][j] == 0:
                    continue
                cur_size = 0      
                
                stack = [(i,j)]
                while len(stack) > 0:
                    # print stack
                    cur = stack.pop()
                    if cur in visited:
                        continue
                    if 0 <= cur[0] < len(grid) and 0 <= cur[1] < len(grid[0]) and grid[cur[0]][cur[1]] > 0:
                        cur_size += 1
                        grid[cur[0]][cur[1]] = cur_component_index
                        # print "adding", cur
                        visited.add(cur)
                        stack.extend([(cur[0]-1, cur[1]), (cur[0]+1,cur[1]), (cur[0],cur[1]-1), (cur[0],cur[1]+1)])
                sizes[cur_component_index] = cur_size
                cur_component_index += 1
                
                
        # print grid
        # print sizes
        output = max(sizes.values())
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # print i,j
                if grid[i][j] == 0:
                    cur_output = 0
                    index_set = set()
                    for cur in [(i-1, j), (i+1,j), (i,j-1), (i,j+1)]:
                        # print "neighbor", cur
                        if 0 <= cur[0] < len(grid) and 0 <= cur[1] < len(grid[0]):
                            index_set.add(grid[cur[0]][cur[1]])
                            
                        # print "sum", cur_output
                    for k in index_set:
                        cur_output += sizes[k]
                    output = max(output, cur_output+1)
                    
        return output
                
                        
                        
                    
