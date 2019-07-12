import sys
from linked_list.double_linked_list import DoubleLinkedList, Node

class BetterLRU:
    """ an LRU implemented with:
        - a queue of values, ordered by last access time (using a doubly linked list)
        - a hash table of key -> (value adress in the queue) for fast lookups
    """
    def __init__(self, size):
        self.size = size
        self.pages_dict = {}
        self.pages_queue = DoubleLinkedList()
        self.stored_pages_count = 0
    
    def put(self, key, value):
        if key in self.pages_dict: #existing node
            node = self.pages_dict[key]
            node.data = (key, value)
            self.move_node_to_first_position(node)
        else: # new node
            if self.is_full():
                self.remove_last_page()
            else:
                self.stored_pages_count += 1
            self.pages_dict[key] = value
            self.pages_queue.prepend(Node((key, value)))

    def is_full(self):
        return self.stored_pages_count >= self.size
    
    def remove_last_page(self):
        node = self.pages_queue.last
        key = node.data[0]
        node.prev.next = None
        self.pages_queue.last = node.prev
        del self.pages_dict[key]

    def get(self, key):
        if key not in self.pages_dict:
            raise RuntimeError("Key not in cache")
        node = self.pages_dict[key]
        self.move_node_to_first_position(node)
        return node.data

    def move_node_to_first_position(self, node):
        if self.pages_queue.head is not node:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.pages_queue.head.next = node
            node.prev = self.pages_queue.head
            self.pages_queue.head = node
        

class LRU:
    
    def __init__(self, size=256):
        self.size = size
        self.cache = {}
        self.last_reads = {}
        self.global_age = 0
        self.stored_count = 0
    
    def get(self, key): # O(1)
        if key not in self.cache:
            return -1
        else:
            self.update_read_hit_age(key)
            return self.cache[key]
    
    def set(self, key, value):  # O(size)
        if self.is_full():
            print("CACHE IS ALREADY FULL")
            self.delete_oldest_page()
        if key not in self.cache:
            self.stored_count += 1
        self.cache[key] = value
        self.update_read_hit_age(key)
    
    def update_read_hit_age(self, key):  # O(1)
        self.last_reads[key] = self.global_age
        self.global_age += 1

    def delete_oldest_page(self):  # O(size)
        oldest_read = sys.maxsize
        oldest_key = None
        for (key, last_read) in self.last_reads.items():
            if last_read < oldest_read:
                oldest_read = last_read
                oldest_key = key
        if oldest_key is not None:
            print("DELETING OLDEST KEY: {} -> {}".format(oldest_key, oldest_read))
            del self.cache[oldest_key]
            del self.last_reads[oldest_key]
            self.stored_count -= 1   

    def is_full(self):  # O(1)
        return self.stored_count == self.size
