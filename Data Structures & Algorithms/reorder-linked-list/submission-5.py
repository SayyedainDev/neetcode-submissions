class Solution:
    def reorderList(self, head):
        if head is None or head.next is None:
            return

        # -----------------------------------
        # Step 1: Find the middle of the list
        # -----------------------------------
        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        # slow is now at the end of the first half
        second = slow.next

        # Break the list into two halves
        slow.next = None

        # -----------------------------------
        # Step 2: Reverse the second half
        # -----------------------------------
        previous = None
        current = second

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        # previous is the head of reversed second half
        second = previous

        # -----------------------------------
        # Step 3: Merge the two halves
        # -----------------------------------
        first = head

        while second is not None:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next