class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        Lprev = dummy
        curr = head

        # Move to the beginning of the section
        for _ in range(left - 1):
            Lprev = Lprev.next
            curr = curr.next

        # Reverse nodes from left to right
        prev = None

        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Reconnect the reversed section
        Lprev.next.next = curr
        Lprev.next = prev

        return dummy.next