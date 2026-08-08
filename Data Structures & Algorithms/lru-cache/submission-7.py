
class Node:
    def __init__(self,data,key):
        self.data=data
        self.key=key
        self.prev=None
        self.next=None



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.freq={}

        self.right=Node(0,0)
        self.left=Node(0,0)
        self.right.prev=self.left
        self.left.next=self.right
    
    def remove(self,node):
        previous=node.prev
        following=node.next
        previous.next=following
        following.prev=previous

    def insert(self,node):
        previous=self.right.prev
        previous.next=node
        node.prev=previous
        node.next=self.right
        self.right.prev=node


        
    def get(self,key):
        if key not in self.freq:
            return -1
        
        node=self.freq[key]
        self.remove(node)
        self.insert(node)
       
        return node.data



    def put(self,key,data):
        if key in self.freq:
            node=self.freq[key]
            node.data=data
            self.remove(node)
            self.insert(node)
            return

        node=Node(data,key)
        self.freq[key]=node
        self.insert(node)
        if len(self.freq)>self.capacity:
            node=self.left.next
            self.remove(node)
            RK=node.key
            del(self.freq[RK])
            



        