class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}  # hashmap of nodes

        # pointer to the least recent used node and most recent used mode
        # initialize them to (0,0) as (key, val)
        self.lru = Node(0,0 )
        self.mru = Node(0,0 )

        # connect lru and mru together
        # first the cache is empty, only has LRU and MRU
        self.lru.next = self.mru
        self.mru.prev = self.lru

    # need some helper functions for remove/insert
    def remove(self, node):
        # remove node from list
        # doubly linked list
        # first save current node's prev and next nodes
        prev, nxt = node.prev, node.next
        # then remove the current node by pointer manipulation
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        # insert node at right
        # prev <----------- mru
        #      -----------> (nxt)
        # prev <-- node <-- mru
        #      -->      -->
        # 
        prev, nxt = self.mru.prev, self.mru
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev


    def get(self, key):
        if key in self.cache:
            # when we get the value, we first remove this node from the list
            self.remove(self.cache[key])
            # then we insert it at right, make it the Most recent used node
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        # if the key is already in the cache
        # first we remove the old node with the same key + old value
        # then we create a new node
        # then we replace it with the new value in the cache
        # then we insert this new node at right
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # check capacity
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from the hashmap
            lru = self.lru.next
            self.remove(lru)
            del self.cache[lru.key]

lrc = LRUCache(2)
print(lrc.put(1,1))
print(lrc.put(2,2))
print(lrc.get(1))
print(lrc.put(3,3))
print(lrc.get(2))
print(lrc.put(4,4))
print(lrc.get(1))
print(lrc.get(3))
print(lrc.get(4))