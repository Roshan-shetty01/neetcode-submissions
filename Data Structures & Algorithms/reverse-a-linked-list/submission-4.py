# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            nxt = curr.next  # 1. Save the next node so we don't lose the rest of the list
            curr.next = prev  # 2. Reverse the pointer direction to point backward
            
            # 3. Move our pointers one step forward for the next iteration
            prev = curr       
            curr = nxt        

        # At the end, 'prev' will be standing at the new head of the reversed list
        return prev