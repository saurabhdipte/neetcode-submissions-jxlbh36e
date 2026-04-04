class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set()
        for num in nums:
            if num not in seen:
                seen.add(num)
        longest=0
        for num in seen:
            if (num-1) not in seen:
                length=1
                nextnum=num+1
                while nextnum in seen:
                    length+=1
                    nextnum+=1
                longest=max(length,longest)
        return longest

            
        