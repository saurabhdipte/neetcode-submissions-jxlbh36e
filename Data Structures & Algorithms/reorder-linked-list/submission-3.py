# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        newhead = slow.next
        
        prev = None
        slow.next = None
        while newhead:
            temp = newhead.next
            newhead.next = prev
            prev =newhead
            newhead = temp
        
        first = head
        second = prev
        while second:
            temp = first.next
            temp2 = second.next
            first.next = second
            second.next = temp
            first = temp
            second = temp2