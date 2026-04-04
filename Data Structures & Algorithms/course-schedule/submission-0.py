class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj={i:[] for i in range(numCourses)}
        visit=set()
        for a,b in prerequisites:
            adj[a].append(b)
        def dfs(a):
            if a in visit:
                return False
            if adj[a]==[]:
                return True
            visit.add(a)
            for b in adj[a]:
                if not dfs(b):
                    return False
            adj[a]=[]
            visit.remove(a)
            return True
        for n in range(numCourses):
            if not dfs(n):
                return False
        return True
                
        