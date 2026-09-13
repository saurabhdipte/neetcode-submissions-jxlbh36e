class TimeMap:

    def __init__(self):
        self.seen = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.seen:
            self.seen[key]=[]
        self.seen[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        result = ''
        values = self.seen.get(key,[])
        left,right = 0,len(values)-1
        while left<=right:
            mid = left + (right-left)//2
            if values[mid][0]<=timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid -1


        return result



        
