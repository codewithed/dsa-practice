class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            # Store next node (before overwriting)
            next_node = current.next
            # Reverse the current node's pointer
            current.next = previous
            # Move pointers one step ahead
            previous = current
            current = next_node
        return previous
