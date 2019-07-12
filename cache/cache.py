import sys


class Page:
    """ a memory page in a cache, with pointers to the previous and next pages """
    def __init__(self, data, previous=None, next=None):
        self.data = data


class BetterLRU:
    """ an LRU implemented with:
        - a queue of values, ordered by last access time (implemented with a doubly linked list)
        - a hash table of key -> (value adress in the queue) for fast lookups
    """
    def __init__(self, size):
        self.size = size
        self.pages_dict = {}
        

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
