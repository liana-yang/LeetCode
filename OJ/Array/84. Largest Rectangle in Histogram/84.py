class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # The main function to find the maximum rectangular area under given histogram with n bars
        # Create an empty stack. The stack holds indexes of hist[] array
        # The bars stored in stack are always in increasing order of their heights.
        stack = []
        maxArea = 0; # Initalize max area
        tp = 0  # To store top of stack
        area_with_top = 0 # To store area with top bar as the smallest bar
        # Run through all bars of given histogram
        i = 0
        while i < len(height):
        # If this bar is higher than the bar on top stack, push it to stack
            if not stack or height[stack[-1]] <= height[i]:
                stack.append(i)
                i += 1
        # If this bar is lower than top of stack, 
        # then calculate area of rectangle with stack top as the smallest (or minimum height) bar. 
        # 'i' is 'right index' for the top and element before top in stack is 'left index'
            else:
                tp = stack[-1]  # store the top index
                stack.pop();  # pop the top
 
            # Calculate the area with hist[tp] stack as smallest bar
            if not stack:
                area_with_top = height[tp] * i
            else:
                area_with_top = height[tp] * (i - stack[-1] - 1);
 
            # update max area, if needed
            maxArea = max(maxArea, area_with_top)

        # Now pop the remaining bars from stack and calculate area with every popped bar as the smallest bar
        while stack:
            tp = stack[-1]
            stack.pop()
            if not stack:
                area_with_top = height[tp] * i
            else:
                area_with_top = height[tp] * (i - stack[-1] - 1);
            maxArea = max(maxArea, area_with_top)
        return maxArea

s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3])

