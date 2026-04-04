class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={i:[] for i in range(numCourses)}
        
        for a,b in prerequisites:
            adj[a].append(b)
        visit=set()
        def dfs(i):
            if i in visit:
                return False
            if adj[i]==[]:
                return True
            visit.add(i)
            for node in adj[i]:
                if dfs(node)==False:
                    return False

            visit.remove(i)
            return True
        for i in range(numCourses):
            if dfs(i)==False:
                return False
        return True