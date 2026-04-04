class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        adj={i: [] for i in range(numCourses)}
        for a,b in prerequisites:
            adj[a].append(b)
        visit=set()
        cycle=set()
        def dfs(a):
            if a in cycle:
                return False
            if a in visit:
                return True
            
            cycle.add(a)
            for b in adj[a]:
                if not dfs(b):
                    return False
            
            
            cycle.remove(a)
            visit.add(a)
            res.append(a)
            return True
        for n in range(numCourses):
            if not dfs(n):
                return []
        return res
