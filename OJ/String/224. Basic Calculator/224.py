class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Simple iterative solution by identifying characters one by one. 
        # One important thing is that the input is valid, 
        # which means the parentheses are always paired and in order. 
        # Only 5 possible input we need to pay attention:
        # digit: it should be one digit from the current number
        # '+': number is over, we can add the previous number and start a new number
        # '-': same as above
        # '(': push the previous result and the sign into the stack, set result to 0, just calculate the new result within the parenthesis.
        # ')': pop out the top two numbers from stack, 
        #      first one is the sign before this pair of parenthesis, 
        #      second is the temporary result before this pair of parenthesis. We add them together.
        # Finally if there is only one number, from the above solution, 
        # we haven't add the number to the result, so we do a check see if the number is zero.
        stack = []
        result = 0
        number = 0
        sign = 1
        for i in range(len(s)):
        	if s[i] == '+':
        		result += sign * number
        		number = 0
        		sign = 1
        	elif s[i] == '-':
        		result += sign * number
        		number = 0
        		sign = -1
        	elif s[i] == '(':
        		# we push the result first, then sign;
        		stack.append(result)
        		stack.append(sign)
        		sign = 1
        		result = 0
        	elif s[i] == ')':
	    		# reset the sign and result for the value in the parenthesis
        		result += sign * number
        		number = 0
        		result *= stack.pop() # stack.pop() is the sign before the parenthesis
        		result += stack.pop() # stack.pop() now is the result calculated before the parenthesis
        	elif s[i] != ' ':
        		number = 10 * number + int(s[i])
        if number != 0:
	    	result += sign * number
        return result

