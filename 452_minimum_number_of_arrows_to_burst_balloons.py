class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points)
        # print points
        
        if len(points) < 2:
            return len(points)
        out = 0
        
        
        last_arrow = 0
        i = 0
        while True:
            if i >= len(points):
                break
            if i == 0 or points[i][0] > last_arrow:
                cur_lo = points[i][0]
                cur_hi = points[i][1]
                
                i += 1
                if i >= len(points):
                    out += 1
                    break
                    
                while True:
                    if points[i][0] > cur_hi:
                        out += 1
                        last_arrow = cur_hi
                        break
                    cur_lo = max(cur_lo, points[i][0])
                    cur_hi = min(cur_hi, points[i][1])
                    
                    i += 1
                    if i >= len(points):
                        out += 1
                        break
                last_arrow = cur_hi
                    
                
#                 next_arrow = points[i][1]
#                 i += 1
#                 if i >= len(points):
#                     out += 1
#                     break
#                 while points[i][1] <= next_arrow:
#                     i += 1
#                     if i >= len(points):
#                         break
#                     next_arrow = points[i][1]
#                 out += 1
#                 last_arrow = next_arrow
#             i += 1
#             if i >= len(points):
#                 break
                
                
        # print out
        return out
