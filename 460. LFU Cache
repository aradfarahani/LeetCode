class Node:
    def __init__(self, key=None, value=None, freq=0):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def is_empty(self):
        return self.head.next == self.tail

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_node = {}
        self.freq_list = {}

    def _update(self, node):
        freq = node.freq
        self.freq_list[freq].remove(node)
        if self.freq_list[freq].is_empty():
            del self.freq_list[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        node.freq += 1
        freq = node.freq
        if freq not in self.freq_list:
            self.freq_list[freq] = DoublyLinkedList()
        self.freq_list[freq].insert_after(self.freq_list[freq].head, node)

    def get(self, key: int) -> int:
        if key not in self.key_node:
            return -1
        node = self.key_node[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_node:
            node = self.key_node[key]
            node.value = value
            self._update(node)
        else:
            if self.size == self.capacity:
                node_to_remove = self.freq_list[self.min_freq].tail.prev
                self.freq_list[self.min_freq].remove(node_to_remove)
                del self.key_node[node_to_remove.key]
                self.size -= 1

            new_node = Node(key, value, 1)
            self.key_node[key] = new_node
            if 1 not in self.freq_list:
                self.freq_list[1] = DoublyLinkedList()
            self.freq_list[1].insert_after(self.freq_list[1].head, new_node)
            self.min_freq = 1
            self.size += 1

# Example usage:
lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))  # Output: 1
lfu.put(3, 3)
print(lfu.get(2))  # Output: -1
print(lfu.get(3))  # Output: 3
lfu.put(4, 4)
print(lfu.get(1))  # Output: -1
print(lfu.get(3))  # Output: 3
print(lfu.get(4))  # Output: 4
