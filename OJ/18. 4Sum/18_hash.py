class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        length = len(nums)
        value = []
        key = []
        hash_length = 0
        nums.sort()
        num1 = []
        num2 = []
        num3 = []
        num4 = []
        count = 0
        hash_table = [[] for i in range(10)]

        if length > 3 and (nums[0] + nums[1] + nums[2] + nums[3] <= target <= nums[length - 1] + nums[length - 2] + nums[length - 3] + nums[length - 4]):
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
                if key[i] > 3:
                    key[i] = 3
                    if count == 0 and value[i] * 4 == target:
                        num1.append(value[i])
                        num2.append(value[i])
                        num3.append(value[i])
                        num4.append(value[i])
                        count += 1
                        key[i] = 2
            for i in range(hash_length):
                if key[i] > 2:
                    key[i] = 2
                    find = target - value[i] * 3
                    mod_find = find % 10
                    for v in hash_table[mod_find]:
                        if v == find and v != value[i]:
                            num1.append(value[i])
                            num2.append(value[i])
                            num3.append(value[i])
                            num4.append(v)
                            count += 1
                            break
            for i in range(hash_length):
                if key[i] > 1:
                    for j in range(i + 1, hash_length):
                        if value[j] * 2 == target - value[i] * 2 and key[j] > 1:
                            num1.append(value[i])
                            num2.append(value[i])
                            num3.append(value[j])
                            num4.append(value[j])
                            count += 1
                            break
                    for j in range(hash_length):
                        find = target - value[i] * 2 - value[j]
                        mod_find = find % 10
                        if j != i:
                            for v in hash_table[mod_find]:
                                if v == find and v != value[i] and v > value[j]:
                                    num1.append(value[i])
                                    num2.append(value[i])
                                    num3.append(value[j])
                                    num4.append(v)
                                    count += 1
                                    break
                    key[i] = 1
                for j in range(i + 1, hash_length):
                    for k in range(j + 1, hash_length):
                        find = target - value[i] - value[j] - value[k]
                        mod_find = find % 10
                        for v in hash_table[mod_find]:
                            if v == find and v > value[k]:
                                num1.append(value[i])
                                num2.append(value[j])
                                num3.append(value[k])
                                num4.append(v)
                                count += 1
                                break


        result = [[] for i in range(count)]    
        for i in range(count):
            result[i].append(num1[i])
            result[i].append(num2[i])
            result[i].append(num3[i])
            result[i].append(num4[i])
            result[i].sort()
        result.sort()


        print "hash_length = %s" % hash_length
        print "count = %s" % count
        print value
        print key
        print hash_table
        print result
        return result