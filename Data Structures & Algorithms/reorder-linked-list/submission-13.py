class Solution:
    def reorderList(self, head):
        if head is None or head.next is None:
            return


        slow,fast=head,head

        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None

        prev=None
        curr=second
        while curr is not None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        first=head
        second=prev
        while second is not None:
             first_temp=first.next
             second_temp=second.next
             first.next=second
             second.next=first_temp

             first=first_temp
             second=second_temp

