class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # rev = head[::-1]
        # return rev
        
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            # print(nxt)
            # print(curr.val)
            # print(curr.next)      
            curr.next = prev 
            # print(curr.next)
            # print(curr)
            prev = curr 
            curr = nxt
        return prev
        
