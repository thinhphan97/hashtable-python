from threading import Thread, Lock
import time

class Singleton(type):
    _instances = None
    def __call__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances

class HashTable(metaclass=Singleton):

    # Create empty bucket list of given size
    def __init__(self, size: int, ttl: int = 5):
        self.size = size
        self.hash_table = self.create_buckets()
        self.ttl = ttl
        self.setup_cron()
        self.lock = Lock()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def get_now(self):
        return time.time()
    
    def get_time_expired(self, ttl):
        return time.time() + ttl
    
    # Insert values into hash map
    def set_val(self, key, val, ttl=None):

        # Get the index from the key
        # using hash function
        hashed_key = hash(key) % self.size
        
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            # check if the bucket has same key as
            # the key to be inserted
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key to be inserted,
        # Update the key value
        # Otherwise append the new key-value pair to the bucket
        time = self.get_now()

        if not ttl:
            ttl = self.ttl
        time_expired = self.get_time_expired(ttl=ttl)

        with self.lock:
            if found_key:
                bucket[index] = (key, {"time": time,
                                       "time_exp": time_expired,
                                       "values": val})
            else:
                bucket.append((key, {"time": time,
                                       "time_exp": time_expired,
                                       "values": val}))

    # Return searched value with specific key
    def get_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
        
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            # check if the bucket has same key as 
            # the key being searched
            if record_key == key:
                found_key = True
                break

        # If the bucket has same key as the key being searched,
        # Return the value found
        # Otherwise indicate there was no record found
        if found_key:
            return record_val["values"]
        else:
            return "No record found"

    # Remove a value with specific key
    def delete_val(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = hash(key) % self.size
        
        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record
            
            # check if the bucket has same key as
            # the key to be deleted
            if record_key == key:
                found_key = True
                break

        with self.lock:
            if found_key:
                bucket.pop(index)

        return found_key

    def delete_cron(self):

        while True:

            time.sleep(1)
            for i in range(self.size):
                bucket = self.hash_table[i]
                for index, record in enumerate(bucket):
                    record_key, record_val = record
                    if record_val["time_exp"] < self.get_now():
                        print(record_key)
                        with self.lock:
                            bucket.pop(index)

    def setup_cron(self):

        t=Thread(target=self.delete_cron, name="Thread_cron_clean_hash_table")
        t.start()
    
    # To print the items of hash map
    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
