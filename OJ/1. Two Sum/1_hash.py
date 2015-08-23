class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def twoSum(self, nums, target):
        length = len(nums)
        num1 = []
        num2 = []
        count = 0
        nums_sorted = sorted(nums)
        value = []
        key = []
        hash_length = 0
        hash_table = [[] for i in range(10)]

        solved = False

        if length > 1 and (nums_sorted[0] + nums_sorted[1] <= target <= nums_sorted[length - 1] + nums_sorted[length - 2]):
            value.append(nums_sorted[0])
            key.append(1)
            hash_length += 1
            hash_table[nums_sorted[0] % 10].append(value[0])
            for i in range(length - 1):
                if nums_sorted[i + 1] != nums_sorted[i]:
                    value.append(nums_sorted[i + 1])
                    key.append(1)
                    hash_length += 1
                else:
                    key[hash_length - 1] += 1
            for i in range(hash_length - 1):
                mod = value[i + 1] % 10
                hash_table[mod].append(value[i + 1])

            for i in range(hash_length):
                if solved == True:
                    break
                if key[i] > 1:
                    key[i] = 1
                    if value[i] * 2 == target:
                        #num1.append(value[i])
                        #num2.append(value[i])
                        num1 = value[i]
                        num2 = value[i]
                        solved = True
                        break
            for i in range(hash_length):
                if solved == True:
                    break
                find = target - value[i]
                mod_find = find % 10
                for v in hash_table[mod_find]:
                    if v == find and v != value[i]:
                    #if v == find and (v != value[i] or key[i] > 2):
                        #num1.append(value[i])
                        #num2.append(v)
                        num1 = value[i]
                        num2 = v
                        solved = True
                        break
        index = []
        for i in range(length):
            if nums[i] == num1:
                index.append(i + 1)
                break
        for i in range(length):
            if nums[i] == num2 and i + 1 != index[0]:
                index.append(i + 1)
                break
        index.sort()
        print value
        print key
        print hash_table
        print index
        return index

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()        
    #s.threeSum([12,13,12,13,-3,3,11,7,10,5,1,6,6,14,2,-8,-1,-4,3,-10,3,-13,7,-15,12,10,-2,-14,3,-3,-7,0,-12,12,-1,0,0,-13,-8,-12,7,0,9,-1,-8,-12,6,6,-1,-13,3,-13,-11,-4,9,-14,-9,14,9,2,-3,-13,9,0,-15,-15,7,-8,-12,6,-5,10,14,-11,-6,-9,14,8,4,-10,10,-8,14,6,3,8,0,2,8,-6,11,12,-3,5,-3,-11,6,11,-4,1,-6,-1,-4,-7,3,-2,-9,-5,-9,10,0,8,-12,-8,-1])
    s.twoSum([-10,-7,-3,-9,-8,-9,-5,6,0,6,4,-15,-12,3,-12,-10,-5,-5,2,-4,13,8,-9,6,-11,11,3,-13,-3,14,-9,2,14,-5,8,-9,-7,-12,5,1,2,-6,1,5,4,-4,3,7,-2,12,10,-3,6,-14,-12,10,12,7,12,-14,-2,11,4,-10,13,-11,-4,-8,-15,-14,8,-6,-12,-14,6,7,-3,-14,-1,11,14,-6,-15,5,-13,-12,0,14,2,-11,-14,8,-15,-3,13,14,-7,-14,13,-15,10,-2,-14,13],0)
    s.twoSum([3, 2, 4], 6)
    finish = clock()
    print (finish - start) * 1000
