class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        N = 0
        current = head
        while current:
            N += 1
            current = current.next

        index = N - n

        
        if index == 0:
            return head.next

        
        current = head
        for _ in range(index - 1):
            current = current.next

        current.next = current.next.next

        return head