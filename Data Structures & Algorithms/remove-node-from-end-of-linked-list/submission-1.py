# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        prev=None
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        head=prev
        current=head
        prev=None
        count=1
        while current:
            if count==n:
                if prev==None:
                    head=current.next
                else:
                    prev.next=current.next
            prev=current
            current=current.next
            count+=1
        current=head
        prev=None
        while current:
            temp=current.next
            current.next=prev
            prev=current
            current=temp
        return prev
        
        
