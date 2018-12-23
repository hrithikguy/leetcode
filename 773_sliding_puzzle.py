swap_lists={}
swap_lists[0] = [1,3]
swap_lists[1] = [0,2,4]
swap_lists[2] = [1, 5]
swap_lists[3] = [0,4]
swap_lists[4] = [1,3,5]
swap_lists[5] = [2,4]

def get_neighbors(node):
    output =[]
    index = node.index(0)

    for i in swap_lists[index]:
        cur =[]
        for j in node:
            cur.append(j)
        t = cur[index]
        cur[index] = cur[i]
        cur[i] = t
        output.append(cur)
    return output

class Solution(object):

    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        start=board[0] + board[1]
        print start
        
        stack = [(start,0)]
        visited = [start]
        while len(stack) > 0:
            cur=stack[0]
            stack = stack[1:]
            print cur
            if cur[0] == [1,2,3,4,5,0]:
                return cur[1]
            neighbors = get_neighbors(cur[0])
            for i in neighbors:
                if i not in visited:
                    stack.append((i, cur[1] +1))
                    visited.append(i)
                    
        return -1
