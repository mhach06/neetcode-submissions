# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1 = l1
        cur_l2 = l2
        remainder = 0

        dummy = ListNode()
        cur_n = dummy

        while cur_l1 or cur_l2 or remainder > 0:
            # Safely grab values or default to 0
            v1 = cur_l1.val if cur_l1 else 0
            v2 = cur_l2.val if cur_l2 else 0

            # Calculate total, carry, and node value
            total = v1 + v2 + remainder
            remainder = total // 10
            new_val = total % 10

            cur_n.next = ListNode(new_val)
            cur_n = cur_n.next

            # Advance pointers safely
            cur_l1 = cur_l1.next if cur_l1 else None
            cur_l2 = cur_l2.next if cur_l2 else None

        return dummy.next



        