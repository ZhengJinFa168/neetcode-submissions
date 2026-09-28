class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in range(len(points)):
            x_i,y_i = points[i][0],points[i][1]
            dist_i = math.sqrt((x_i)**2 + (y_i)**2)
            heapq.heappush(distances,(dist_i,[x_i,y_i]))
        
        res = []
        for i in range(k):
            min_k, coords = heapq.heappop(distances)
            res.append(coords)
        
        return res