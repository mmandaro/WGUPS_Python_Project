# HashTable class using chaining, found in the WGU C950 Zybooks text figure 7.8.2 with modification for this project
class ChainingHashTable:

    # initialize the hash table to a list of empty lists
    def __init__(self, initial_size=10):
        self.table = []
        for i in range(initial_size):
            self.table.append([])

    # create a way to insert items into the hashtable, where the key is the package id
    def insert(self, key, item):
        #bucket is assigned with an index based on package id modulo size of hash table (default is 10)
        bucket = hash(key) % len(self.table)
        #assign the location in the hash table using the location found above
        bucket_list = self.table[bucket]

        # see if the key exists in the bucket already, and update its value if found
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = item
                return True

        # if the key is not already in the bucket list, add it to the end
        key_item = [key, item]
        bucket_list.append(key_item)
        return True

    # search for an item by its package id number. Returns the package data if found, or None if not found
    def search(self, package_id):
        # use the hash equation to obtain the bucket this package id would correspond to
        bucket = hash(package_id) % len(self.table)
        # obtain the list at the bucket we found above
        bucket_list = self.table[bucket]

        # search for the package id in the bucket list
        for key_value in bucket_list:
            if key_value[0] == package_id:  # for each key and value pair at this bucket list, check for package id
                return key_value[1]  # if the package id is found, return the package information, i.e. the value

        return None  # if the key was not found, the item is not in the hash table so return None

    #remove a package from the hash table by finding it by its package id
    def remove(self, package_id):
        # get the bucket list where the package will be removed
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # if the package is found, remove it from the bucket list
        if package_id in bucket_list:
            bucket_list.remove(package_id)




