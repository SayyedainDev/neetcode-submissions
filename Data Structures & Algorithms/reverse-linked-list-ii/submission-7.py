class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        leftprev=dummy
        curr=dummy.next
        for _ in range(left-1):
            leftprev=curr
            curr=curr.next
            
        
        prev=None
        for _ in range(right-left+1):
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        leftprev.next.next=curr
        leftprev.next=prev
        return dummy.next
        


       