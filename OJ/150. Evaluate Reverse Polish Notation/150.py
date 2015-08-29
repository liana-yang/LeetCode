class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        result = 0
        length = len(tokens)
        if length == 1:
            return int(tokens[0])
        for i in range(length):
            if tokens[i] == '+':
                result = int(stack[- 2]) + int(stack[- 1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == '-':
                result = int(stack[- 2]) - int(stack[- 1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == '*':
                result = int(stack[- 2]) * int(stack[- 1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == '/':
                result = int(float(stack[- 2]) / int(stack[- 1]))
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(tokens[i])
        return result
        

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()   
    print s.evalRPN(["3","-4","+"])
    finish = clock()
    print (finish - start) * 1000