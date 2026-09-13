"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.seen_nodes = {}  # original_node -> cloned_node

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        if head in self.seen_nodes:
            return self.seen_nodes[head]

        # Create clone and record it before recursing to prevent infinite loops
        clone = Node(head.val)
        self.seen_nodes[head] = clone

        clone.next = self.copyRandomList(head.next)
        clone.random = self.copyRandomList(head.random)

        return clone



