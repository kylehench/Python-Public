# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4

class LRUCache:

  def __init__(self, capacity: int):
    self.cache = {}
    self.capacity = capacity
    # list of keys in order of creation date. Value of -1 indicates deleted key/updated use history.
    self.cache_creation_arr = []
    # start index variable for performance (values in middle of array are not deleted)
    self.cache_creation_arr_start_i = 0
    # used to lookup index of keys in cache_creation_arr. {key: index}
    self.cache_creation_dict = {}

  def update_cache_history(self, key, key_present=True):
    if key_present:
      self.cache_creation_arr[self.cache_creation_dict[key]] = -1
    self.cache_creation_arr.append(key)
    self.cache_creation_dict[key] = len(self.cache_creation_arr)-1

  def get(self, key: int) -> int:
    if key in self.cache:
      self.update_cache_history(key)
      return self.cache[key]
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self.cache[key] = value
      self.update_cache_history(key)
    else:
      # free space in cache if cache is full
      if len(self.cache) == self.capacity:
        while self.cache_creation_arr[self.cache_creation_arr_start_i] == -1:
          self.cache_creation_arr_start_i += 1
        key_evict = self.cache_creation_arr[self.cache_creation_arr_start_i]
        del self.cache[key_evict]
        del self.cache_creation_dict[key_evict]
        self.cache_creation_arr_start_i += 1

      self.cache[key] = value
      self.update_cache_history(key, key_present=False)