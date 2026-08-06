# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        
        Second=slow.next
        slow.next=None
        prev=None
        while Second:
            temp=Second.next
            Second.next=prev
            prev=Second
            Second=temp
        
        Second=prev
        first=head
        while Second:
            first_temp=first.next
            Second_temp=Second.next
            first.next=Second
            Second.next=first_temp

            first=first_temp
            Second=Second_temp
            


        

        