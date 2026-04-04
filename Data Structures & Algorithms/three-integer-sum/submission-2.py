class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count=Counter(nums)
        res=[]
        keys=sorted(count.keys())
        for i in range(len(keys)):
            a=keys[i]
            for j in range(i,len(keys)):
                b=keys[j]
                c=-(a+b)
                if c not in count:
                    continue
                if b>c:
                    continue
                if (a==b==c):
                    if count[a]>=3:
                        res.append([a,b,c])
                elif (a==b!=c):
                    if(count[a]>=2 and count[c]>=1 ):
                        res.append([a,b,c])
                elif(a!=b==c):
                    if(count[a]>=1 and count[b]>=2):
                        res.append([a,b,c])
                else:
                    if(count[a]>=1 and count[b]>=1 and count[c]>=1):
                        res.append([a,b,c])
        return res


        