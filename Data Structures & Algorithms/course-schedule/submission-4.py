class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for u,v in prereq:
            adj[u].append(v)

        visit = set()

        def dfs(csr):
            if csr in visit:
                return False
            if adj[csr] == []:
                return True
            visit.add(csr) 
            for pre in adj[csr]:
                if dfs(pre) == False:
                    return False
            adj[csr] = []
            visit.remove(csr)
            return True
        for crs in range(n):
            if dfs(crs) == False:
                return False
        return True
        