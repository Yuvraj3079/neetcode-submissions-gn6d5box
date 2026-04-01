class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distanceAndPoints = []
        for x, y in points:
            distance = x*x + y*y
            distanceAndPoints.append((distance,[x,y]))
        
        heapq.heapify(distanceAndPoints)
        res = []
        while k > 0:
            dis, points = heapq.heappop(distanceAndPoints)
            res.append(points)
            k -= 1
        return res
