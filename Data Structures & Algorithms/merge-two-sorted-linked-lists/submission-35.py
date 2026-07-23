class Solution:
    def mergeTwoLists(self, list1, list2):
        # Dummy node makes building the result easier
       dummy=ListNode(-1)
       curr=dummy
       if list1 is None:
          return list2
       elif list2 is None:
          return list1
       while list1 and list2 :
          v1= list1.val 
          v2 = list2.val 
          if v1 <= v2:
              curr.next=ListNode(v1)
              list1=list1.next if list1 else None
          else:
            curr.next=ListNode(v2)
            list2 =list2.next if list2 else None
          curr=curr.next
        
       while list1:
          curr.next=ListNode(list1.val)
          list1=list1.next
          curr=curr.next
       while list2:
          
          curr.next=ListNode(list2.val)
          list2=list2.next
          curr=curr.next
          
       return dummy.next
