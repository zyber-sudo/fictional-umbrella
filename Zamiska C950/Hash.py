# Hash table module


class ChainingHashTable:
    """
    Class to create, edit, and delete items in a chaining hash table.

    Big-O: O(n)
    """

    def __init__(self, initial_capacity=10):
        """
        The initializing function when one creates a new hash table (chaining).

        :param initial_capacity: The desired capacity of the new hash table.

        Big-O: O(n)
        """

        self.table = []
        for j in range(initial_capacity):
            self.table.append([])

    def insert(self, key, item):
        """
        Function to add an item into the already created hash table. The function runs it through the hash equation
        and then appends it to the hash table at the location given by that equation.

        :param key: The key value desired for the corresponding item.
        :param item: The object/item that will be added to the hash table associated with the given ID.
        :return: True to signal the action is completed.

        Big-O: O(n)
        """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    def search(self, key):
        """
        Function used to obtain a specific element from the hash table by using the items ID.

        :param key: The key of the value that is being searched for.
        :return: If the key value exist, the corresponding item. If not, it returns none.

        Big-O: O(n)
        """

        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:

            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        """
        Function used to remove an item from the hash table. (This as of 10/10/2022 is not being used in the program.)

        :param key: The key of the item that is to be removed.

        Big-O: O(n)
        """
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
