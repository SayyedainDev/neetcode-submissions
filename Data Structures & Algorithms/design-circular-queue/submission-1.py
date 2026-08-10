class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None





class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity=k
        self.size=0
        self.left=Node(0)
        self.right=Node(0)
        self.left.next=self.right
        self.right.prev=self.left
        


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node=Node(value)
        previous=self.right.prev
        previous.next=node
        node.next=self.right
        self.right.prev=node
        node.prev=previous
        self.size+=1
    
        return True

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        following=self.left.next
        node=following.next
        node.prev=self.left
        self.left.next=node
        
        self.size-=1
        return True
       
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        node=self.left.next
        return node.data
        
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        node=self.right.prev
        return node.data
    
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
     
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()