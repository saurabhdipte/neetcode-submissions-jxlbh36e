class ListNode():
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            oldnode=self.cache[key]
            self.remove(oldnode)
        node=ListNode(key,value)
        self.cache[key]=node
        self.add(node)
        if len(self.cache)>self.capacity:
            nodetodelete=self.head.next
            self.remove(nodetodelete)
            del self.cache[nodetodelete.key]
    
    def add(self,node):
        prevend=self.tail.prev
        prevend.next=node
        node.next=self.tail
        node.prev=prevend
        self.tail.prev=node
    
    def remove(self,node):
        prevend=node.prev
        nextnode=node.next
        prevend.next=nextnode
        nextnode.prev=prevend
        
