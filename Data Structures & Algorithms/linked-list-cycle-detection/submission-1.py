# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head.next

        while slow is not None or fast is not None:
            if slow == fast:
                return True
            
            if slow is not None and slow.next is not None:
                slow = slow.next
            else:
                slow = None
            
            if fast is not None and fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
            else:
                fast = None
        
        return False
        

