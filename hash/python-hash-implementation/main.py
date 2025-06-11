# this uses an open addressing so doesnt solve the collision problems
import hashlib
class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()


    def get_position(self, key):
        encoded_key = key.encode("utf-8")
        sha_256_key = hashlib.sha256(encoded_key).digest()
        int_number = int.from_bytes(sha_256_key)
        hashed_key =  int_number % self.size
        return hashed_key

    def create_buckets(self):
        return [[] for _ in range(self.size)]
    
    def set_val(self, key, val):

        
        hashed_key = self.get_position(key)

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
        hashed_key = self.get_position(key)

        bucket = self.hash_table[hashed_key]
        


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
        hashed_key = self.get_position(key)

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
    
hash_tab = HashTable(50)

hash_tab.set_val("gabriel@gmail.com", {})

print(hash_tab.get_position("gabriel@gmail.com"))
print(hash_tab.get_val("gabriel@gmail.com"))
print(hash_tab)


