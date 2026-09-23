class ListNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity = capacity
        self.tail = ListNode(-1,-1)
        self.head  = ListNode(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.removenode(node)
        self.addnode(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key  in self.cache:
            nodetodel = self.cache[key]
            self.removenode(nodetodel)
        node=ListNode(key,value)
        self.cache[key]=node
        self.addnode(node)
        while len(self.cache)>self.capacity:
            nodetodel = self.head.next
            self.removenode(nodetodel)
            del self.cache[nodetodel.key]


    def addnode(self,node):
        prevnode=self.tail.prev
        prevnode.next = node
        node.prev=prevnode
        node.next=self.tail
        self.tail.prev=node

    def removenode(self,node):
        prevnode=node.prev
        prevnode.next=node.next
        node.next.prev=prevnode
        
        

    
        
