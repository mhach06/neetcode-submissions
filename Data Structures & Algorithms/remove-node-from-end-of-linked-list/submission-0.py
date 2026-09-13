# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head
        total_n = 1

        while cur.next:
            cur = cur.next
            total_n += 1
        
        node_i = total_n - n + 1

        count = 1
        cur = head
        prev = None

        while count != node_i:
            prev = cur
            cur = cur.next

            count += 1
        
        if cur and cur.next:
            next = cur.next
            cur.next = None
        else:
            next = None

        if prev != None:
            prev.next = next
        else:
            head = next
            
        return head
        

