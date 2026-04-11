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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i,e in enumerate(edges):
            e.append(i)
        edges.sort(key = lambda x:x[2])
        mst_cost=0
        uf=unionFind(n)
        for u,v,w,i in edges:
            if uf.union(u,v) == True:
                mst_cost+=w
        critical=[]
        p_critical=[]




        for n1,n2,w,i in edges:
            #critical
            cost=0
            uf=unionFind(n)
            for v1,v2,weight,j in edges:
                if   i!=j and uf.union(v1,v2) :
                    cost+=weight
            if cost>mst_cost or max(uf.rank)!=n:
                critical.append(i)
                continue

            #pcritical
            uf =unionFind(n)
            cost=w
            uf.union(n1,n2)
            for v1,v2 , weight,j in edges:
                if uf.union(v1,v2):
                    cost+=weight
            if cost==mst_cost:
                p_critical.append(i)
        return [critical,p_critical]



        
