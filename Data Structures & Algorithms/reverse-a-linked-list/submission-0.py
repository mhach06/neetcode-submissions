# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Handle empty list or single-node list
        if not head or not head.next:
            return head

        prev = head
        head = head.next
        next = head.next
        
        # Crucial: point the old first node to None so it doesn't create a cycle
        prev.next = None 

        while head is not None:
            head.next = prev

            prev = head

            head = next

            if head and head.next:
                next = head.next
            else:
                next = None

        return prev

