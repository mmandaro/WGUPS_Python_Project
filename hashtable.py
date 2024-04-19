class ChainingHashTable:
    """
    HashTable class using chaining, found in the WGU C950 Zybooks text figure 7.8.2 with modification for this
    project.
    """
    def __init__(self, initial_size=10):
        """Initialize the hash table to a list of empty lists, which represent the 'buckets'."""
        self.table = []
        for i in range(initial_size):
            self.table.append([])

    def insert(self, key, item):
        """# Method to insert items into the hashtable, where the key is the package id."""
        # Bucket is assigned with an index based on the package id modulo size of hash table (default is 10)
        bucket = hash(key) % len(self.table)
        # Assign the location in the hash table using the location found above
        bucket_list = self.table[bucket]

        # See if the key exists in the bucket already, and update its value if found
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = item
                return True

        # If the key is not already in the bucket list, add it to the end
        key_item = [key, item]
        bucket_list.append(key_item)
        return True

    def search(self, package_id):
        """Method to search for an item by its id number. Returns the package data if found, or None if not found."""
        # Use the hash equation to obtain the bucket this package id would correspond to
        bucket = hash(package_id) % len(self.table)
        # Obtain the list at the bucket we found above
        bucket_list = self.table[bucket]

        # Search for the package id in the bucket list
        for key_value in bucket_list:
            # For each key and value pair at this bucket list, check for package id
            if key_value[0] == package_id:
                # If the package id is found, return the package information, i.e. the value
                return key_value[1]
        # If the key was not found, the item is not in the hash table so return None
        return None

    def remove(self, package_id):
        """Remove a package from the hash table after finding it using its package id."""
        # Get the bucket list where the package will be removed
        bucket = hash(package_id) % len(self.table)
        bucket_list = self.table[bucket]

        # If the package is found, remove it from the bucket list
        if package_id in bucket_list:
            bucket_list.remove(package_id)




