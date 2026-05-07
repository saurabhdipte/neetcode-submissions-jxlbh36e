class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = dummy    
        cur = head

        
        for _ in range(left - 1):
            prev = cur
            cur = cur.next
        
        tail = cur
        prev_rev = None
        for _ in range(right - left + 1):
                temp = cur.next
                cur.next = prev_rev
                prev_rev = cur
                cur = temp
        prev.next = prev_rev
        tail.next =cur
        return dummy.next

        