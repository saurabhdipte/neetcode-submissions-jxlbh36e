# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous=None
        current=head
        while current:
            temp=current.next
            current.next=previous
            previous=current
            current=temp
        reverse_head=previous
        current=reverse_head
        previous=None
        count=1
        while current:
            if count==n:
                if previous is None:
                    reverse_head=current.next
                else:
                    previous.next=current.next
                break
            previous=current
            current=current.next
            count+=1
        previous=None
        current=reverse_head
        while current:
            temp=current.next
            current.next=previous
            previous=current
            current=temp
        return previous
                  
         
            
                    

        



