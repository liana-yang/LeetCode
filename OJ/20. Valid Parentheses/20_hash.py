class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        result = True
        length = len(s)
        hash_table = [[] for i in range(6)]
        nums = [0 for i in range(6)]
        for i in range(length):
            if length % 2 == 1 or length == 0:
                result = False
                break
            if s[i] == '(':
                hash_table[0].append(i)
                nums[0] += 1
            if s[i] == ')':
                hash_table[1].append(i)
                nums[1] += 1 
            if s[i] == '[':
                hash_table[2].append(i)
                nums[2] += 1 
            if s[i] == ']':
                hash_table[3].append(i) 
                nums[3] += 1
            if s[i] == '{':
                hash_table[4].append(i) 
                nums[4] += 1
            if s[i] == '}':
                hash_table[5].append(i)
                nums[5] += 1

        if result == True:
            for i in range(3):
                if nums[i * 2] != nums[i * 2 + 1]:
                    result = False
                    break
        print hash_table
        if result == True:
            for i in range(3):
                for j in range(nums[i * 2 + 1]):
                    for k in range(nums[i * 2]):
                        if hash_table[i * 2][k] > hash_table[i * 2 + 1][j]:
                            if k == 0:
                                result = False
                                break
                            else:
                                for l in range(k):
                                    if (hash_table[i * 2][k - 1 - l] - hash_table[i * 2 + 1][j]) % 2 == 1 and hash_table[i * 2][k - 1 - l] != - 1:
                                        hash_table[i * 2][k - 1 - l] = - 1
                                        hash_table[i * 2 + 1][j] = - 1
                                        break
                            break
                        elif k == nums[i * 2] - 1:
                            for l in range(k + 1):
                                if (hash_table[i * 2][k - l] - hash_table[i * 2 + 1][j]) % 2 == 1 and hash_table[i * 2][k - l] != - 1:
                                    hash_table[i * 2][k - l] = - 1
                                    hash_table[i * 2 + 1][j] = - 1
                                    break

                    if hash_table[i * 2 + 1][j] != - 1:
                        result = False
                        break
                if result == False:
                    break
               
        print hash_table
        print nums
        print result
        return result

if __name__=='__main__':
    from time import clock
    start = clock()
    #for i in range(1000000):
        #test()
    s = Solution()        
    #s.isValid('[({(())}[()])]')
    s.isValid('[()](())')
    #s.isValid('([]]')
    #s.isValid('()[]{}')
    #s.isValid('([])')
    finish = clock()
    print (finish - start) * 1000