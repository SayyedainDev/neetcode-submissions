class Node:
    def __init__(self,value,key):
        self.value=value
        self.key=key
        self.prev=None
        self.next=None




class LRUCache:

    def __init__(self, capacity: int):
        self.freq={}
        self.capacity=capacity
        self.right=Node(0,0)
        self.left=Node(0,0)
        
        self.left.next=self.right
        self.right.prev=self.left

    def remove(self,node):
        previous=node.prev
        following=node.next
        previous.next=following
        following.prev=previous

    def insert(self,node):
        prev=self.right.prev
        self.right.prev=node
        prev.next=node
        node.prev=prev
        node.next=self.right

    def get(self,key):
        if key not in self.freq:
            return -1
        
        node=self.freq[key]
        self.remove(node)
        self.insert(node)     
        return node.value   

    


    def put(self,key,value):
        if key  in self.freq:
            node=self.freq[key]
            node.value=value
            self.remove(node)
            self.insert(node)
            
        else:
            node=Node(value,key)
            self.freq[key]=node
            self.insert(node)
            if len(self.freq)>self.capacity:
                least_recent=self.left.next
                kl=least_recent.key
                del(self.freq[kl])
                self.remove(least_recent)



        