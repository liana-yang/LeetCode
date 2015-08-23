class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        length = len(nums)
        num1 = []
        num2 = []
        num3 = []
        count = 0
        nums.sort()  
        value = []
        key = []
        hash_length = 0
        hash_table = [[] for i in range(10)]

        if length > 2 and (nums[0] + nums[1] + nums[2] <= 0 <= nums[length - 1] + nums[length - 2] + nums[length - 3]):
            value.append(nums[0])
            key.append(1)
            hash_length += 1
            hash_table[nums[0] % 10].append(value[0])
            for i in range(length - 1):
                if nums[i + 1] != nums[i]:
                    value.append(nums[i + 1])
                    key.append(1)
                    hash_length += 1
                else:
                    key[hash_length - 1] += 1
            for i in range(hash_length - 1):
                mod = value[i + 1] % 10
                hash_table[mod].append(value[i + 1])

            for i in range(hash_length):
                #if key[i] > 2:
                    #key[i] = 2
                    #if count == 0 and value[i] == 0:
                        #num1.append(0)
                        #num2.append(0)
                        #num3.append(0)
                        #count += 1
                        #key[i] = 1
            #for i in range(hash_length):
                if key[i] > 1:
                    #key[i] = 1
                    find = 0 - value[i] * 2
                    mod_find = find % 10
                    for v in hash_table[mod_find]:
                        #if v == find and v != value[i]:
                        if v == find and (v != value[i] or key[i] > 2):
                            num1.append(value[i])
                            num2.append(value[i])
                            num3.append(v)
                            count += 1
                            break
                for j in range(i + 1, hash_length):
                    find = 0- value[i] - value[j]
                    mod_find = find % 10
                    for v in hash_table[mod_find]:
                        if v == find and v > value[j]:
                            num1.append(value[i])
                            num2.append(value[j])
                            num3.append(v)
                            count += 1
                            break
    
        result = [[] for i in range(count)]    
        for i in range(count):
            result[i].append(num1[i])
            result[i].append(num2[i])
            result[i].append(num3[i])
            result[i].sort() 

        result.sort()
        print "count = %s" % count
        print value
        print key
        print result
        return result

if __name__=='__main__':
    from time import time
    start = time()
    #for i in range(1000000):
        #test()
    s = Solution()        
    #s.threeSum([12,13,12,13,-3,3,11,7,10,5,1,6,6,14,2,-8,-1,-4,3,-10,3,-13,7,-15,12,10,-2,-14,3,-3,-7,0,-12,12,-1,0,0,-13,-8,-12,7,0,9,-1,-8,-12,6,6,-1,-13,3,-13,-11,-4,9,-14,-9,14,9,2,-3,-13,9,0,-15,-15,7,-8,-12,6,-5,10,14,-11,-6,-9,14,8,4,-10,10,-8,14,6,3,8,0,2,8,-6,11,12,-3,5,-3,-11,6,11,-4,1,-6,-1,-4,-7,3,-2,-9,-5,-9,10,0,8,-12,-8,-1])
    s.threeSum([-10,-7,-3,-9,0,-8,-9,-5,6,0,6,4,-15,-12,3,-12,-10,-5,-5,2,-4,13,8,-9,6,-11,11,3,-13,-3,14,-9,2,14,-5,8,-9,-7,-12,5,1,2,-6,1,5,4,-4,3,7,-2,12,10,-3,6,-14,-12,10,12,7,12,-14,-2,11,4,-10,13,-11,-4,-8,-15,-14,8,-6,-12,-14,6,7,-3,-14,-1,11,14,-6,-15,5,-13,-12,0,14,2,-11,-14,8,-15,-3,13,14,-7,-14,13,-15,10,-2,-14,13])
    #s.threeSum([0,3,0,1,1,-1,-5,-5,3,-3,-3,0])
    finish = time()
    print (finish - start) * 1000

#s = Solution()        
#s.threeSum([12,13,12,13,-3,3,11,7,10,5,1,6,6,14,2,-8,-1,-4,3,-10,3,-13,7,-15,12,10,-2,-14,3,-3,-7,0,-12,12,-1,0,0,-13,-8,-12,7,0,9,-1,-8,-12,6,6,-1,-13,3,-13,-11,-4,9,-14,-9,14,9,2,-3,-13,9,0,-15,-15,7,-8,-12,6,-5,10,14,-11,-6,-9,14,8,4,-10,10,-8,14,6,3,8,0,2,8,-6,11,12,-3,5,-3,-11,6,11,-4,1,-6,-1,-4,-7,3,-2,-9,-5,-9,10,0,8,-12,-8,-1])
