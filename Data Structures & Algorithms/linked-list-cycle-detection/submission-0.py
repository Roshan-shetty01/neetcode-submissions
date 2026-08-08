# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        
        while current:
            # If we've already seen this exact node before, it's a cycle
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        
        # We reached the end (null), so no cycle
        return False