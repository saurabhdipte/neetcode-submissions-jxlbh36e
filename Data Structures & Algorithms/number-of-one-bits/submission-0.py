class Solution:
    def hammingWeight(self, n: int) -> int:
        result=0
        while n:
            result = result + (n%2)
            n = n >>1
        return result
