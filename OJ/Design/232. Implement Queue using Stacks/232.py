class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        Queue.queue = []
        Queue.first = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.queue:
            self.first = x
        self.queue.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.remove(self.first)
        if self.queue:
            self.first = self.queue[0]

    def peek(self):
        """
        :rtype: int
        """
        return self.first
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.queue:
            return True
        else:
            return False
        