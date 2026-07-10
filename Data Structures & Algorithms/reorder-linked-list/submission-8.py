class Solution:
    def reorderList(self, head):
        if head is None or head.next is None:
            return

        # Step 1: Find the middle
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split the two halves
        second = slow.next
        slow.next = None

        # Step 3: Reverse the second half
        curr = second
        prev = None

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # prev is the new head of the reversed half
        second = prev
        first = head

        # Step 4: Merge both halves
        while second is not None:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2