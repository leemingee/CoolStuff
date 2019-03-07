# Created by Ming Li at 3/6/2019

# Feature: 

# Description:

# Contact: ming.li2@columbia.edu


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict
class LRUCache_1(OrderedDict):
    '''
        we need to think about this question using our understanding of the data structure.
        so for this problem, we have few targets to be achieved.

        We're asked to implement the structure which provides the following operations in \mathcal{O}(1)O(1) time :

        - Get the key / Check if the key exists
        - Put the key
        - Delete the first added key

        The first two operations in O(1) time are provided by the standard hashmap,
        and the last one - by linked list.

        There is a structure called ordered dictionary,
        it combines behind both hashmap and linked list.
        In Python this structure is called OrderedDict and in Java LinkedHashMap.
    '''
    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

class LRUCache_2:

    def __init__(self, capacity):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass

class LRUCache_0:
    # this one will work, but due to some list operation, like
    # list.remove is not O(1) time, so will runtime error on leetcode
    # but the functionality is fine

    def __init__(self, capacity: int):
        self.used_dict = {}
        self.capacity = capacity
        self.lastusedkey = []

    def get(self, key: int) -> int:
        if key in self.used_dict:
            self.lastusedkey.remove(key)
            self.lastusedkey.append(key)
            return self.used_dict[key]
        else:
            # self.lastusedkey.append(key)
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.used_dict) == self.capacity:
            leastRecentUsedKey = self.lastusedkey[0]
            del self.used_dict[leastRecentUsedKey]
            self.lastusedkey.remove(leastRecentUsedKey)
        self.lastusedkey.append(key)
        self.used_dict[key] = value

if __name__ == '__main__':
    capacity = 2
    # obj = LRUCache_0(capacity)
    obj = LRUCache_1(capacity)
    obj.put(1, 1)
    obj.put(2, 2)
    obj.get(1)
    obj.put(3, 3)
    obj.get(2)
    obj.put(4, 4)
    obj.get(1)
    obj.get(3)
    obj.get(4)