class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        myheap = []
        res=-1
        heapq.heappush(myheap, (grid[0][0], (0,0)))
        while len(myheap) > 0:
            bestneighbor, (i,j) = heapq.heappop(myheap)
            # print (i,j)
            res = max(res, bestneighbor)
            if (i,j)== (len(grid)-1,len(grid[0])-1):
                return res
            
            grid[i][j] = -1
            if i > 0 and grid[i-1][j] >= 0:
                heapq.heappush(myheap, (grid[i-1][j], (i-1,j)))
            if i < len(grid)-1 and grid[i+1][j] >= 0:
                heapq.heappush(myheap, (grid[i+1][j], (i+1,j)))
            if j > 0 and grid[i][j-1] >= 0:
                heapq.heappush(myheap, (grid[i][j-1], (i,j-1)))
            if j < len(grid[0])-1 and grid[i][j+1] >= 0:
                heapq.heappush(myheap, (grid[i][j+1], (i,j+1)))
            # print myheap
            # print grid
                
