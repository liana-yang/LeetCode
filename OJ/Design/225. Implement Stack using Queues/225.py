import Queue
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        Stack.stack = Queue.Queue()
        Stack.last = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.put(x)
        self.last = x
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack.qsize() > 1:
            for i in range(self.stack.qsize() - 2):
                temp = self.stack.get()
                self.stack.put(temp)
            self.last = self.stack.get()
            self.stack.put(self.last)
        self.stack.get()
        
    def top(self):
        """
        :rtype: int
        """
        return self.last
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack.empty()
        