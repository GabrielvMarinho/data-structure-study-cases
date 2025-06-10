# this uses an open addressing so doesnt solve the collision problems

class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self, key, val):
        # uses siphash as the hash function
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]

        found_key = False

        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    def get_val(self, key):
        hashed_key = hash(key) % self.size

        bucket = self.hash_table[hashed_key]
        
        #???????????????????????????????
        print(bucket)


        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break

        if found_key:
            return record_val
        else:
            return "no record found"
        
    def delete_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket.pop(index)
        return
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
    
hash_tab = HashTable(2)

hash_tab.set_val("gabriel@gmail.com", {})
print(hash_tab)


print(hash_tab)
print(hash_tab)
print(hash_tab)
print(hash_tab)
print(hash_tab)