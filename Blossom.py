from linked_list import Node, LinkedList

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [None for i in range(self.array_size)]

    def hash(self, key):
        key_code = key.encode()
        hash_code = sum(key_code)
        return hash_code
    
    def compress(self, hash_code):
        return hash_code % self.array_size
    
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        self.array[array_index] = [key, value]

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        payload = self.array[array_index]

        if payload != None:
            if payload[0] == key:
                return payload[1]
            else:
                return None
        else:
            return None