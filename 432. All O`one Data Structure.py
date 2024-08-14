class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.key_count = {}
        self.count_node = {}
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, prev_node, new_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.count_node[node.count]

    def inc(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            self.key_count[key] += 1
            self.count_node[count].keys.remove(key)
            if count + 1 not in self.count_node:
                new_node = Node(count + 1)
                self.count_node[count + 1] = new_node
                self._add_node(self.count_node[count], new_node)
            self.count_node[count + 1].keys.add(key)
            if not self.count_node[count].keys:
                self._remove_node(self.count_node[count])
        else:
            self.key_count[key] = 1
            if 1 not in self.count_node:
                new_node = Node(1)
                self.count_node[1] = new_node
                self._add_node(self.head, new_node)
            self.count_node[1].keys.add(key)

    def dec(self, key: str) -> None:
        count = self.key_count[key]
        self.key_count[key] -= 1
        self.count_node[count].keys.remove(key)
        if self.key_count[key] == 0:
            del self.key_count[key]
        else:
            if count - 1 not in self.count_node:
                new_node = Node(count - 1)
                self.count_node[count - 1] = new_node
                self._add_node(self.count_node[count].prev, new_node)
            self.count_node[count - 1].keys.add(key)
        if not self.count_node[count].keys:
            self._remove_node(self.count_node[count])

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

# Example usage:
allOne = AllOne()
allOne.inc("hello")
allOne.inc("hello")
print(allOne.getMaxKey())  # Output: "hello"
print(allOne.getMinKey())  # Output: "hello"
allOne.inc("leet")
print(allOne.getMaxKey())  # Output: "hello"
print(allOne.getMinKey())  # Output: "leet"
