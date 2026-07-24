class Solution:
    def mergeTwoLists(self, list1, list2):
        # Dummy node makes building the result easier
       dummy=ListNode(-1)
       curr=dummy
       while list1 and list2:
            if list1.val >= list2.val:
               curr.next=ListNode(list2.val)
               list2=list2.next
            else:
               curr.next=ListNode(list1.val)
               list1=list1.next
            curr=curr.next
       curr.next =list1 if list1 else list2
       return dummy.next

