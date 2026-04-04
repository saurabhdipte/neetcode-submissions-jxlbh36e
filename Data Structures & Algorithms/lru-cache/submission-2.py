class ListNode():

    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=self.prev=None



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.cache={}
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
            nodetodel=self.cache[key]
            self.remove(nodetodel)
        node=ListNode(key,value)
        self.cache[key]=node
        self.add(node)
        while len(self.cache)>self.capacity:
            nodetodel=self.head.next
            self.remove(nodetodel)
            del self.cache[nodetodel.key]    

    def remove(self,node):
        prevnode=node.prev
        prevnode.next=node.next
        node.next.prev=prevnode

    def add(self,node):
        prevnode=self.tail.prev
        prevnode.next=node
        node.prev=prevnode
        node.next=self.tail
        self.tail.prev=node

        
        
