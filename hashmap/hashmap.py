import array

class HashMap():
    def __init__(self, size=256):
        self.keys_array_size = size
        self.keys_array = [[] for i in range(0, self.keys_array_size)]
    
    def get(self, key):
        hashed_key = hash(key)
        position = self.calculate_position(hashed_key)
        for (current_key, value) in self.keys_array[position]:
            if current_key == key:
                return value
        raise RuntimeError
    
    def add(self, key, value):
        hashed_key = hash(key)
        position = self.calculate_position(hashed_key)
        self.keys_array[position].append((key, value))
    
    def calculate_position(self, hashed_key):
        return hashed_key % self.keys_array_size