# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1, 2, 3, 4, 5, 6], k=3
# [prev, cur, 2, 3, 4, 5, 6], count=1
# [prev, cur, next, 3, 4, 5, 6], count=1
# [prev <- cur, next -> 3 ...] count=1
# [dummy <- prev, cur -> 3 -> 4 ...], count=2
# [dummy <- prev, cur -> next -> 4 -> 5 -> 6], count=2
# [dummy <- prev <- cur, next -> 4 -> 5 -> 6], count=2
# [dummy <- 1 <- prev, cur -> 4 -> 5 -> 6], count=3
# [dummy <- 1 <- prev, cur -> next -> 5 -> 6], count=3
# [dummy <- 1 <- prev <- cur, next -> 5 -> 6], count=3
# [dummy <- 1 (head) <- 2 <- prev, cur -> 5 -> 6], count=3
# if not at last node
# tail = prev
# head.next = tail of next reverse (self.reverse(cur, k))

# [3 -> 2 -> 1 -> : prev, cur -> 5 -> 6], count=1
# [3 -> 2 -> 1 -> : prev, cur -> next -> 6], count=1
# [3 -> 2 -> 1 -> : prev <- cur, next -> 6], count=1
# [3 -> 2 -> 1 -> : dummy <- prev, cur -> 6], count=2
# [3 -> 2 -> 1 -> : dummy <- prev, cur -> next], count=2
# [3 -> 2 -> 1 -> : dummy <- prev <- cur, next], count=2
# [3 -> 2 -> 1 -> : dummy <- 4 <- prev, cur], count=3
# [3 -> 2 -> 1 -> : dummy <- 4 <- prev, cur, next=null], count=3
# [3 -> 2 -> 1 -> : dummy <- 4 <- prev <- cur, next=null], count=3
# [3 -> 2 -> 1 -> : dummy <- 4 <- 5 <- prev, cur=null], count=3
# head.next = null (since last node) and return tail (prev)

# 3 -> 2 -> 1 -> 6 -> 5 -> 4 -> null


class Solution:   

    def is_valid_nodes(self, cur, k):
        count = 0
        while cur and count != k:
            cur = cur.next
            count += 1
        
        return count == k

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        cur = head
        dummy = ListNode()
        prev = dummy
        count = 1

        if not self.is_valid_nodes(head, k):
            return head

        while count <= k and cur:
            next = cur.next # next node, keep track
            cur.next = prev # reverse
            prev = cur
            cur = next

            count += 1
        
        tail = prev
        if cur:
            head.next = self.reverseKGroup(cur, k)
        else:
            head.next = None
        
        return tail
        