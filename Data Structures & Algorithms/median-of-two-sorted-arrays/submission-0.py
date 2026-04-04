class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>=len(nums2):
            b=nums1
            a=nums2
        else:
            b=nums2
            a=nums1
        total=len(a)+len(b)
        half=total//2
        l,r=0,len(a)-1
        while True:
            ma=l + (r-l)//2
            mb=half-ma-2
            aleft=a[ma] if ma>=0 else float("-inf")
            bleft=b[mb] if mb>=0 else float("-inf")
            aright=a[ma+1] if ma+1<len(a) else float("inf")
            bright=b[mb+1] if mb+1<len(b) else float("inf")
            if bleft<=aright and aleft<=bright:
                if total%2==0:
                    return (max(aleft,bleft) + min(aright,bright))/2
                else:
                    return min(aright,bright)
            elif aleft>bright:
                r=ma-1
            else:
                l=ma+1