class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        MinStack.stack = []
        MinStack.min = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:
            self.stack.append(0)
            self.min = x
        else:
            self.stack.append(x - self.min) # Could be negative if min value needs to change
            if x < self.min:
                self.min = x
        

    def pop(self):
        """
        :rtype: nothing
        """
        if not self.stack:
            return None
        temp = self.stack.pop()
        if temp < 0:
            self.min -= temp # If negative, increase the min value
        

    def top(self):
        """
        :rtype: int
        """
        temp = self.stack[-1]
        if temp > 0:
            return temp + self.min
        else:
            return self.min
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
    # The question is ask to construct One stack. So I am using one stack.
    # The idea is to store the gap between the min value and the current value;
    # The problem for my solution is the cast. 
    # I have no idea to avoid the cast. 
    # Since the possible gap between the current value 
    # and the min value could be Integer.MAXVALUE-Integer.MINVALUE;

s = MinStack()
s.push(-2)
s.push(0)
s.push(-1)
print s.getMin
print s.top
print s.pop
print s.getMin
print s.stack
        