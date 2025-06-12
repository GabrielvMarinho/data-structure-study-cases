# this uses an open addressing so doesnt solve the collision problems
import hashlib
class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[("",{})] for i in range(self.size)]

    def get_position(self, key):
        encoded_key = key.encode("utf-8")
        sha_256_key = hashlib.sha256(encoded_key).digest()
        int_number = int.from_bytes(sha_256_key)
        hashed_key =  int_number % self.size
        return hashed_key
    
    def get_next_free_position(self, key, val, position):

        if position <= self.size-1: 
            bucket = self.hash_table[position]

            if bucket != [] or bucket == [("-", {})]:
                return self.get_next_free_position(key, val, position+1)
            else:
                return position
                
        else:
            print("not enough spaces! recalculate")
    
    def set_val(self, key, val):

        hashed_key = self.get_position(key)
        bucket = self.hash_table[hashed_key]

    
        if bucket == []:
            bucket.insert(hashed_key, (key, val))
        elif bucket != [(key, val)]:
            position = self.get_next_free_position(key, val, hashed_key)
            self.hash_table[position] = [(key, val)]
        else:
            print("already exist")
            
    def get_next_position_equals(self, key, position):

        key_bucket, value_bucket = self.hash_table[position][0]
        if position <= self.size-1:
          
            if(key_bucket != "-" or key_bucket != key):
                return self.get_next_position_equals(key, position+1)                    
            else:
                return position

        else:
            print("not enough spaces! recalculate")

    def get_val(self, key):
        hashed_key = self.get_position(key)

        bucket = self.hash_table[hashed_key]
        key_bucket, value_bucket = bucket[0]

        if(bucket):
            if(key_bucket == key):
                return bucket
            else:
                position = self.get_next_position_equals(key, hashed_key)
                return self.hash_table[position]
        else:
            return "no record found"
    
    def delete_val(self, key):
        hashed_key = self.get_position(key)
        key_bucket, value_bucket = self.hash_table[hashed_key][0]
        if(key_bucket == key):
            self.hash_table[hashed_key] = [("-",{})]
        else:
            self.hash_table[self.get_next_position_equals(key, hashed_key)] = [("-",{})]
            
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
    
hash_tab = HashTable(3)



hash_tab.set_val("gabriel@gmail.com", {})




print(hash_tab)
