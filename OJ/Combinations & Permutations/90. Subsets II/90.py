class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return []
        nums.sort() #sort the array to avoid descending list of int
        res = [[]]
        for element in nums:
            temp = []
            for ans in res:
                 #append the new int to each existing list
                if ans + [element] not in res:
                    temp.append(ans + [element])
            res += temp
        return res
        
if __name__=='__main__':
    from time import clock
    start = clock()
    s = Solution()
    print s.subsetsWithDup([1,2,2])
    finish = clock()
    print (finish - start) * 1000