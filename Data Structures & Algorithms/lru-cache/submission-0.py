class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # key -> Node
        self.cache = {}

        # Dummy boundary nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left


    # Remove a node from its current position
    def remove(self, node):
        previous = node.prev
        following = node.next

        previous.next = following
        following.prev = previous


    # Add a node before right
    # This makes it the most recently used node
    def insert(self, node):
        previous = self.right.prev

        previous.next = node
        node.prev = previous

        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # The node was used, so move it to the recent side
        self.remove(node)
        self.insert(node)

        return node.value


    def put(self, key: int, value: int) -> None:

        # Key already exists
        if key in self.cache:
            node = self.cache[key]

            node.value = value

            # Move it to the recent side
            self.remove(node)
            self.insert(node)

        # Key does not exist
        else:
            new_node = Node(key, value)

            self.cache[key] = new_node
            self.insert(new_node)

        # Cache has exceeded its capacity
        if len(self.cache) > self.capacity:

            # First real node is least recently used
            least_recent = self.left.next

            self.remove(least_recent)

            # Also remove it from hashmap
            del self.cache[least_recent.key]