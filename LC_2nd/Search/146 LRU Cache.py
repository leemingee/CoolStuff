# Created by Ming Li at 3/6/2019

# Feature: 

# Description:

# Contact: ming.li2@columbia.edu


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache_1:
    '''
    we need to think about this question using our understanding of the data structure.
    so for this problem, we have few targets to be achieved.

    '''
    def __init__(self, capacity):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass

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