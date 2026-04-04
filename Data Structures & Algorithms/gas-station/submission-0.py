class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        n=len(gas)
        res=0
        total=0
        for i in range(n):
            total+=(gas[i]-cost[i])
            if total<0:
                total=0
                res=i+1
        return res
