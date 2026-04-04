# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total=0
        current=head
        while current:
            total+=1
            current=current.next
        n=total-n
        if n==0:
            return head.next
        current=head
        for i in range(0,n):
            if (i+1)==n:
                current.next=current.next.next
                break
            current=current.next
        return head
            




