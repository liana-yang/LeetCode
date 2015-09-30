class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if nums == []:
            return []
        nums.sort() #sort the array to avoid descending list of int
        res = [[]]
        for element in nums:
            temp = []
            for ans in res:
                 #append the new int to each existing list
                temp.append(ans + [element])
            res += temp
        return res
        
        
        


if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.subsets([1,2,3,4])
    finish = clock()
    print (finish - start) * 1000