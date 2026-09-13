
class LRUCache:

  class Node:

    def __init__(self, key: int = 0, val: int = 0):
      self.key = key
      self.val = val
      self.prev: Optional[LRUCache.Node] = None
      self.next: Optional[LRUCache.Node] = None

  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache: dict[int, LRUCache.Node] = {}

    # Dummy boundary nodes: Head (MRU) <-> Tail (LRU)
    self.head = self.Node()
    self.tail = self.Node()
    self.head.next = self.tail
    self.tail.prev = self.head

  # --- Internal Linked List Helpers ---

  def _remove(self, node: Node) -> None:
    """Unlink an existing node from the doubly linked list."""
    prev_node = node.prev
    next_node = node.next
    prev_node.next = next_node
    next_node.prev = prev_node

  def _add_to_head(self, node: Node) -> None:
    """Insert a node right after the dummy head (mark as MRU)."""
    node.prev = self.head
    node.next = self.head.next

    self.head.next.prev = node
    self.head.next = node

  def _move_to_head(self, node: Node) -> None:
    """Mark an existing node as most recently used."""
    self._remove(node)
    self._add_to_head(node)

  def _pop_tail(self) -> Node:
    """Evict and return the least recently used node before the dummy tail."""
    lru_node = self.tail.prev
    self._remove(lru_node)
    return lru_node

  # --- Public API ---

  def get(self, key: int) -> int:
    if key not in self.cache:
      return -1

    node = self.cache[key]
    self._move_to_head(node)
    return node.val

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      # Key exists: update value and move to MRU position
      node = self.cache[key]
      node.val = value
      self._move_to_head(node)
    else:
      # Key does not exist: create and insert at head
      new_node = self.Node(key, value)
      self.cache[key] = new_node
      self._add_to_head(new_node)

      # Evict LRU if capacity exceeded
      if len(self.cache) > self.capacity:
        lru_node = self._pop_tail()
        del self.cache[lru_node.key]

        

