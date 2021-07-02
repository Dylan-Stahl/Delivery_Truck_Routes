class ChainingHashTable:
    def __init__(self, initial_capacity=49):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Does insert and update
    def insert(self, key, item):
        # bucket index is calculated
        bucket = hash(key) % len(self.table)

        # bucket_list accesses the array in which the key and item will be stored
        bucket_list = self.table[bucket]

        # Performs update on key if the key already exists
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Returns value given a key
    def search(self, key):
        # bucket index is calculated
        bucket = hash(key) % len(self.table)

        # bucket_list accesses the array in which the key and item are assumed to be stored
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                # If the item with the correct key if found, the value is returned, if no keys match the argument,
                # then None is returned
                return key_value[1]
        return None

    # Removes a key and a value given a key
    def remove(self, key):
        # bucket index is calculated
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove(key_value[0], key_value[1])

    # Returns the number of bucket_lists in the table
    def hash_size(self):
        i = 0
        for bucket_list in self.table:
            i = i + 1
        return i
