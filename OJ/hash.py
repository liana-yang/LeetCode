hash_table = [[] for i in range(10)] 
        for num in nums:
            m = num % 10
            hash_table[m].append(num)
        for array in hash_table:
            array.sort()


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
    