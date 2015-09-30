class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        length = len(nums)
        num1 = []
        num2 = []
        num3 = []
        count = 0
        sorted_nums = sorted(nums)
        odd_nums = []
        even_nums = []
        length_odd = 0
        length_even = 0
        target_odd = 0
        target_even = 0

        for n in sorted_nums:
            if n % 2 == 1:
                odd_nums.append(n)
                length_odd += 1
            else:
                even_nums.append(n)
                length_even += 1

        if length_even > 2:
            for i in range(length_even):
                target_even = - even_nums[i]
                #if target_even > even_nums[length_even - 1] + even_nums[length_even - 2]:
                    #break
                if target_even >= even_nums[0] + even_nums[1] and (i == 0 or (i != 0 and even_nums[i] != even_nums[i - 1])):
                    even_even_front = -2
                    even_even_back = -2
                    for j in range(length_even):
                        if even_nums[j] == target_even / 2 or even_nums[j] > target_even / 2:
                            even_even_front = j - 1
                            break
                    for j in range(length_even):
                        if even_nums[length_even - 1 - j] == target_even / 2 or even_nums[length_even - 1 - j] < target_even / 2:
                            even_even_back = length_even - j
                            break
    
                    if -1 <= even_even_front <= length_even and -1 <= even_even_back <= length_even:                        
                        if even_even_back - even_even_front > 2:
                            if target_even != 0 or even_even_back - even_even_front > 3:                        
                                num1.append(target_even / 2)
                                num2.append(target_even / 2)
                                num3.append(even_nums[i])
                                count += 1
                        for j in range(0, even_even_front + 1):
                            if even_nums[even_even_front - j] <= even_nums[i]:
                                break
                            else:
                                for k in range(even_even_back, length_even):
                                    if even_nums[k] > target_even - even_nums[0]:
                                        break
                                    elif even_nums[k] == target_even - even_nums[even_even_front - j] and k != i and even_even_front - j != i and (even_even_front - j == even_even_front or (even_even_front - j != even_even_front and (even_nums[even_even_front - j] != even_nums[even_even_front - j + 1] or even_even_front - j + 1 == i))) and (k == even_even_back or (k != even_even_back and (even_nums[k] != even_nums[k - 1] or k - 1 == i))):
                                        num1.append(even_nums[k])
                                        num2.append(even_nums[even_even_front - j])
                                        num3.append(even_nums[i])
                                        count += 1
        
        if length_odd > 1 and length_even > 0:
            for i in range(length_odd):
                if length_odd == 2 and length_even == 1:
                        if odd_nums[0] + odd_nums[1] + even_nums[0] == 0:
                            num1.append(odd_nums[0])
                            num2.append(odd_nums[1])
                            num3.append(even_nums[0])
                            count += 1  
                            break
                #if target_odd > odd_nums[length_odd - 1] + even_nums[length_even - 1]:
                    #break   
                if target_odd >= odd_nums[0] + even_nums[0] and (i == 0 or (i != 0 and odd_nums[i] != odd_nums[i - 1])):
                    target_odd = -odd_nums[i]
                    odd_even_front = -2
                    odd_even_back = -2
                    odd_odd_front = -2
                    odd_odd_back = -2

                    for j in range(length_even):
                        if even_nums[j] > (target_odd / 2 + 0.5):
                            odd_even_front = j - 1
                            odd_even_back = j
                            break
                        else:
                            odd_even_front = length_even - 1

                    for j in range(length_odd):
                        if odd_nums[j] > (target_odd / 2 + 0.5):
                            odd_odd_front = j - 1
                            odd_odd_back = j
                            break
                        else:
                            odd_odd_front = length_odd - 1
    
                    if -1 <= odd_even_front <= length_even and -1 <= odd_odd_back <= length_odd:
                        for j in range(0, odd_even_front + 1):
                            if even_nums[odd_even_front - j] < target_odd - odd_nums[length_odd - 1]:
                                break
                            else:
                                for k in range(odd_odd_back, length_odd):
                                    if odd_nums[k] > target_odd - even_nums[0]:
                                        break
                                    elif odd_nums[k] >= odd_nums[i] and odd_nums[k] == target_odd - even_nums[odd_even_front - j] and k != i and (odd_even_front - j == odd_even_front or (odd_even_front - j != odd_even_front and even_nums[odd_even_front - j] != even_nums[odd_even_front - j + 1])) and (k == odd_odd_back or (k != odd_odd_back and (odd_nums[k] != odd_nums[k - 1] or k - 1 == i))):
                                        num1.append(odd_nums[k])
                                        num2.append(even_nums[odd_even_front - j])
                                        num3.append(odd_nums[i])
                                        count += 1    
                    if -1 <= odd_odd_front <= length_odd and -1 <= odd_even_back <= length_even:
                        for j in range(0, odd_odd_front + 1):
                            if odd_nums[odd_odd_front - j] < odd_nums[i]:
                                break
                            else:
                                for k in range(odd_even_back, length_even):
                                    if even_nums[k] > target_odd - odd_nums[0]:
                                        break
                                    elif even_nums[k] == target_odd - odd_nums[odd_odd_front - j] and odd_odd_front - j != i and (odd_odd_front - j == odd_odd_front or (odd_odd_front - j != odd_odd_front and (odd_nums[odd_odd_front - j] != odd_nums[odd_odd_front - j + 1] or odd_odd_front - j + 1 == i))) and (k == odd_even_back or (k != odd_even_back and even_nums[k] != even_nums[k - 1])):
                                        num1.append(even_nums[k])
                                        num2.append(odd_nums[odd_odd_front - j])
                                        num3.append(odd_nums[i])
                                        count += 1    
    
        result = [[] for i in range(count)]    
        for i in range(count):
            result[i].append(num1[i])
            result[i].append(num2[i])
            result[i].append(num3[i])
            result[i].sort() 

        #result.sort()
        #print odd_nums
        #print even_nums  
        #print "count = %s" % count
        #print "finally = %s" % len(result_unique)
        print result
        return result

if __name__=='__main__':
    from time import time
    start = time()
    #for i in range(1000000):
        #test()
    s = Solution()        
    #s.threeSum([12,13,12,13,-3,3,11,7,10,5,1,6,6,14,2,-8,-1,-4,3,-10,3,-13,7,-15,12,10,-2,-14,3,-3,-7,0,-12,12,-1,0,0,-13,-8,-12,7,0,9,-1,-8,-12,6,6,-1,-13,3,-13,-11,-4,9,-14,-9,14,9,2,-3,-13,9,0,-15,-15,7,-8,-12,6,-5,10,14,-11,-6,-9,14,8,4,-10,10,-8,14,6,3,8,0,2,8,-6,11,12,-3,5,-3,-11,6,11,-4,1,-6,-1,-4,-7,3,-2,-9,-5,-9,10,0,8,-12,-8,-1])
    s.threeSum([-10,-7,-3,-9,-8,-9,-5,6,0,6,4,-15,-12,3,-12,-10,-5,-5,2,-4,13,8,-9,6,-11,11,3,-13,-3,14,-9,2,14,-5,8,-9,-7,-12,5,1,2,-6,1,5,4,-4,3,7,-2,12,10,-3,6,-14,-12,10,12,7,12,-14,-2,11,4,-10,13,-11,-4,-8,-15,-14,8,-6,-12,-14,6,7,-3,-14,-1,11,14,-6,-15,5,-13,-12,0,14,2,-11,-14,8,-15,-3,13,14,-7,-14,13,-15,10,-2,-14,13])
    #s.threeSum([0,3,0,1,1,-1,-5,-5,3,-3,-3,0])
    finish = time()
    print (finish - start) * 1000

#s = Solution()        
#s.threeSum([12,13,12,13,-3,3,11,7,10,5,1,6,6,14,2,-8,-1,-4,3,-10,3,-13,7,-15,12,10,-2,-14,3,-3,-7,0,-12,12,-1,0,0,-13,-8,-12,7,0,9,-1,-8,-12,6,6,-1,-13,3,-13,-11,-4,9,-14,-9,14,9,2,-3,-13,9,0,-15,-15,7,-8,-12,6,-5,10,14,-11,-6,-9,14,8,4,-10,10,-8,14,6,3,8,0,2,8,-6,11,12,-3,5,-3,-11,6,11,-4,1,-6,-1,-4,-7,3,-2,-9,-5,-9,10,0,8,-12,-8,-1])
