            ref = abs(nums[0] + nums[1] + nums[2] - target)
            num1 = nums[0]
            num2 = nums[1]
            num3 = nums[2]
            for i in range(length):
                if ref == 0:
                    break
                front = i + 1
                back = length - 1
                while(back > front):
                    gap = nums[i] + nums[front] + nums[back] - target
                    if abs(gap) < ref:
                        num1 = nums[i]
                        num2 = nums[front]
                        num3 = nums[back]
                        ref = abs(gap)
                    if gap > 0:
                        back -= 1
                    elif gap < 0:
                        front += 1
                    else:
                        break