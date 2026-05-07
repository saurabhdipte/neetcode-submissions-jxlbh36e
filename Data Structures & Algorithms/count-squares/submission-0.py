class CountSquares:

    def __init__(self):
        self.ptscount = collections.defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        self.ptscount[tuple(point)]+=1

        

    def count(self, point: List[int]) -> int:
        res = 0
        qx,qy = point
        for x,y in self.pts:
            if abs(qx - x ) != abs(qy - y) or qx == x or qy ==y:
                continue
            else:
                res += self.ptscount[(x,qy)] * self.ptscount[(qx,y)]
        return res

        
