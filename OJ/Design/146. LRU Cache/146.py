class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.used = 0
        self.cache = {}
        self.stack = []
        
    # @return an integer
    def get(self, key):
        if self.cache.has_key(key):
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache[key]
        else:
            return - 1
        

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if self.get(key) == - 1:
            if self.used == self.capacity:
                delkey = self.stack.pop(0)
                del self.cache[delkey]
                self.cache[key] = value
                self.stack.append(key)
            else:
                self.cache[key] = value
                self.stack.append(key)
                self.used += 1
        else:
            self.cache[key] = value #update the value of the key


if __name__=='__main__':
    from time import clock
    start = clock()
    s = LRUCache

    finish = clock()
    print (finish - start) * 1000