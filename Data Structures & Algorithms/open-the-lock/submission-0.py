class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        def children(code):
            res=[]
            for i in range(4):
                digit=str((int(code[i]) + 1  ) % 10)
                res.append( code[:i] + digit + code[i+1:])
                digit=str((int(code[i]) - 1 + 10 ) % 10)
                res.append( code[:i] + digit + code[i+1:])
            return res



        visit=set(deadends)
        q=deque()
        q.append(('0000',0))
        while q:
            code,turns=q.popleft()
            if code==target:
                return turns
            for child in children(code):
                if child not in visit:
                    visit.add(child)
                    q.append((child,turns+1))
        return -1
