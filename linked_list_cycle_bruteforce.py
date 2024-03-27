class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nextNode = head
        nodes = []
        while nextNode:
            if nextNode.next in nodes:
                return True
            nodes.append(nextNode)
            nextNode = nextNode.next
        return False
