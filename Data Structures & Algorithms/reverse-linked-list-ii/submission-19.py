# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) ->        Optional[ListNode]:
       dummy=ListNode(head,0)
       curr=dummy.next
       Lprev=dummy
       for _ in range(left-1):
        Lprev=Lprev.next
        curr=curr.next
    
        prev=None
        for _ in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        Lprev.next.next=curr
        Lprev.next=prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) ->        Optional[ListNode]:
       dummy=ListNode(0,head)
       curr=dummy.next
       LPrev=dummy

       for _ in range(left-1):
            LPrev=LPrev.next
            curr=curr.next
        
       prev=None

       for _ in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp

       LPrev.next.next=curr
       LPrev.next=prev
       return dummy.next
       



        

        