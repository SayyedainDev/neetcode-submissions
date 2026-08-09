class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None





class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity=k
        self.size=0
        self.left=ListNode(0)
        self.right=ListNode(0)

        self.left.next=self.right
        self.right.prev=self.left


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node=ListNode(value)
        previous=self.right.prev
        
        previous.next=node
        node.next=self.right
        node.prev=previous
        self.right.prev=node
        self.size +=1
        return True

        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        following=self.left.next
        node=following.next
        self.left.next=node
        node.prev=self.left
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
        if self.size == self.capacity:
            return True
        else :
            return False

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()