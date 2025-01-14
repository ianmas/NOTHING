class simplehashmap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size) ]
        
    def hashmap_function(self,key):
        numeric_sum = sum(int(char)for char in key if char.isdigit())
        return numeric_sum % 10
    def put(self, key, value):
        index = self.hashmap_function(key)
        bucket = self.buckets[index]
        for i,(k, v)in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return 
        bucket.append((key, value))
    def get(self,key):
        index = self.hashmap_function(key)
        bucket = self.buckets[index]
        for k,v in bucket:
            if k ==key:
                return v
        return None
    def remove(self,key):
        index = self.hashmap_fuunction
        bucket = self.buckets[index]
        for i,(k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return 
        
    def print_map(self):
        print("hash map contents:")
        for index, bucket in enumerate(self.buckets):
            print(f"buckets {index}: {bucket}")
            
hash_map = simplehashmap()

hash_map.put("123-4567", "Charlotte")
hash_map.put("123-4568", "Thomas")
hash_map.put("123-4569", "Jens")
hash_map.put("123-4570", "Peter")
hash_map.put("123-4571", "Lisa")
hash_map.put("123-4672", "Adele")
hash_map.put("123-4573", "Michaela")
hash_map.put("123-6574", "Bob")

hash_map.print_map()

print("\nName associated with '123-4570':", hash_map.get("123-4570"))

print("Updating the name for '123-4570' to 'James'")
hash_map.put("123-4570","James")

print("Name associated with '123-4570':", hash_map.get("123-4570"))
