class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res=collections.defaultdict(list)
        for index,element in enumerate(nums):
            res[element].append(index)
        for number,indexes in res.items():
            if len(indexes)>=2:
                for i in range(len(indexes)- 1):
                    if abs(indexes[i] - indexes[(i+1)])<=k:
                        return True
        return False