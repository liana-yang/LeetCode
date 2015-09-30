class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        length = len(nums)
        index_target = -1
        index_half = -1
        index1 = -1
        index2 = -1
        num1 = -1
        num2 = -1
        solved = False
        new_nums = sorted(nums)

        for i in range(length):
            if new_nums[i] > target / 2:
                index_half = i - 1
                break
        for i in range(length - index_half):
            if new_nums[length - 1 - i] == target - new_nums[0] + 1:
                index_target = length - i
                break
            elif new_nums[length - 1 - i] < target - new_nums[0] + 1:
                index_target = length - 1 - i
                break

        for i in range(index_half + 1):
            for j in range(index_target - index_half + 1):
                if new_nums[index_target - j] == target - new_nums[i]:
                    num1 = new_nums[i]
                    num2 = new_nums[index_target - j]
                    solved = True
                    break
            if solved == True:
                break

        if num1 == num2:
            for i in range(length):
                if nums[i] == num1 and index1 == -1:
                        index1 = i + 1
                elif nums[i] == num2:
                    index2 = i + 1
                    break
        else:
            for i in range(length):
                if nums[i] == num1:
                    index1 = i + 1
                elif nums[i] == num2:
                    index2 = i + 1
                if index1 != -1 and index2 != -1:
                    break

        if index1 > index2:
            temp = index1
            index1 = index2
            index2 = temp
        index = [index1, index2]
        print index
        return index1, index2

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()        
    #s.threeSum([12,13,12,13,-3,3,11,7,10,5,1,6,6,14,2,-8,-1,-4,3,-10,3,-13,7,-15,12,10,-2,-14,3,-3,-7,0,-12,12,-1,0,0,-13,-8,-12,7,0,9,-1,-8,-12,6,6,-1,-13,3,-13,-11,-4,9,-14,-9,14,9,2,-3,-13,9,0,-15,-15,7,-8,-12,6,-5,10,14,-11,-6,-9,14,8,4,-10,10,-8,14,6,3,8,0,2,8,-6,11,12,-3,5,-3,-11,6,11,-4,1,-6,-1,-4,-7,3,-2,-9,-5,-9,10,0,8,-12,-8,-1])
    s.twoSum([-10,-7,-3,-9,-8,-9,-5,6,0,6,4,-15,-12,3,-12,-10,-5,-5,2,-4,13,8,-9,6,-11,11,3,-13,-3,14,-9,2,14,-5,8,-9,-7,-12,5,1,2,-6,1,5,4,-4,3,7,-2,12,10,-3,6,-14,-12,10,12,7,12,-14,-2,11,4,-10,13,-11,-4,-8,-15,-14,8,-6,-12,-14,6,7,-3,-14,-1,11,14,-6,-15,5,-13,-12,0,14,2,-11,-14,8,-15,-3,13,14,-7,-14,13,-15,10,-2,-14,13],0)
    finish = clock()
    print (finish - start) * 1000