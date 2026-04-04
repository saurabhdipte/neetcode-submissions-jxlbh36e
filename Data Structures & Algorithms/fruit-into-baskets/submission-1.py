class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        seen=collections.defaultdict(int)
        total,res,l=0,0,0
        for r in range(len(fruits)):
            seen[fruits[r]]+=1
            total+=1
            while len(seen)>2:
                seen[fruits[l]]-=1
                total-=1
                if seen[fruits[l]]==0:
                    seen.pop(fruits[l])
                l+=1
                
            res=max(total,res)
        return res