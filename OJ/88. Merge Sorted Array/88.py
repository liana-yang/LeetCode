class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        nums = []
        hash_length = 0
        key = - 1
        if m > 0:
            nums.append([nums1[0], 1])
            hash_length += 1
            for i in range(m - 1):
                if nums1[i + 1] != nums1[i]:
                    nums.append([nums1[i + 1], 1])
                    hash_length += 1
                else:
                    nums[hash_length - 1][1] += 1
        length = len(nums1)
        while(length != 0):
            del nums1[length - 1]
            length -= 1
        if n > 0:
            for i in range(hash_length):
                if nums[i][0] == nums2[0]:
                    key = i
            if key != - 1:
                nums[key][1] += 1
            else:
                nums.append([nums2[0], 1])
                hash_length += 1
            for i in range(n - 1):
                if nums2[i + 1] == nums2[0]:
                    if key != -1:
                        nums[key][1] += 1
                    else:
                        nums[hash_length - 1][1] += 1
                else:
                    if nums2[i + 1] != nums2[i]:
                        nums.append([nums2[i + 1], 1])
                        hash_length += 1
                    else:
                        nums[hash_length - 1][1] += 1
        nums.sort()
        for i in range(hash_length):
            for j in range(nums[i][1]):
                nums1.append(nums[i][0])

        print nums
        #print "key = %s" % key
        print "hash_length = %s" % hash_length

        print nums1
        print nums2

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()        
    #s.merge([1, 3, 5, 5, 15], 5, [1, 1, 2, 6], 4)
    s.merge([0], 0, [1], 1)
    finish = clock()
    print (finish - start) * 1000