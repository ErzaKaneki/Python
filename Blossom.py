from linked_list import Node, LinkedList

class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(self.array_size)]

    def hash(self, key):
        key_code = key.encode()
        hash_code = sum(key_code)
        return hash_code
    
    def compress(self, hash_code):
        return hash_code % self.array_size
    
    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]

        for item in list_at_array:
            if item[0] == key:
                item[1] = value
            else:
                list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]

        for item in list_at_index:
            if item == key:
                return item[1]
            else:
                return None