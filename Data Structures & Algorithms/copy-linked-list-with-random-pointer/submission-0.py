"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy={None:None}

        cur=head
        while cur:
            copyNode=Node(cur.val)
            copy[cur]=copyNode
            cur=cur.next
        cur=head
        while cur:
            copyNode=copy[cur]
            copyNode.next=copy[cur.next]
            copyNode.random=copy[cur.random]
            cur=cur.next
        return copy[head]




        