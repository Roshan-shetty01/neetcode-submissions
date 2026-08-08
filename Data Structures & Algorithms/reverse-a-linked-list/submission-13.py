class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # rev = head[::-1]
        # return rev
        
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev
        
