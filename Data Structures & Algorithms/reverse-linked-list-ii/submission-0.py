# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        curr,Lprev=head,dummy
        for i in range(left-1):
            curr,Lprev=curr.next,curr
        
        #phase 2

        prev=None
        for i in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        

        #phase 3
        Lprev.next.next=curr
        Lprev.next=prev
        return dummy.next

        