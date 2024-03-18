class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n=len(points)
        prev=points[0]
        for i in range (1,n):
            curr=points[i]
            if prev[1]>=curr[0]:
                n-=1
                prev=[curr[0],min(curr[1],prev[1])]
            else:
                prev=curr
        return n
