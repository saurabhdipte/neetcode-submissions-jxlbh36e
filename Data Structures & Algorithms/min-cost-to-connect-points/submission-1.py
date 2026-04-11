class unionFind:
    def __init__(self,n):
        self.par= [ i for i in range(n)]
        self.rank=[1]*n
    def find(self,n1):
        res=n1
        while res!=self.par[res]:
            res=self.par[res]
        return res
    def union(self,n1,n2):
        p1,p2=self.find(n1),self.find(n2)
        if p1==p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.par[p2]=p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1]=p2
            self.rank[p2]+=self.rank[p1]
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        uf=unionFind(n)
        edges=[]
        for i in range(n):
            x1,y1=points[i]
            for j in range(i+1,n):
                x2,y2=points[j]
                dist=abs(x2-x1) + abs(y2-y1)
                edges.append([dist,i,j])
                edges.append([dist,j,i])
        edges.sort(key = lambda x:x[0])
        res=0
        for dist,u,v in edges:
            if uf.union(u,v)==True:
                res+=dist
        return res        