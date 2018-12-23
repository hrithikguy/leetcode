class Solution(object):
    def distance(self, A, B):
        return (A[0] - B[0]) * (A[0] - B[0]) + (A[1] - B[1]) * (A[1] - B[1])
    
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dists = [[0] * len(points) for i in range(len(points))]
        for i in range(len(points)):
            for j in range(len(points)):
                dists[i][j] = self.distance(points[i], points[j])
                
        out = 0
        for i in range(len(points)):
            distsi = {}
            for j in range(len(points)):
                if i == j:
                    continue
                curdist = self.distance(points[i], points[j])
                if curdist in distsi:
                    distsi[curdist] += 1
                else:
                    distsi[curdist] = 1
                    
                    
                    
            for key in distsi:
                out += distsi[key] * (distsi[key] - 1)
                
        return out
