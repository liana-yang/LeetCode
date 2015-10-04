class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        stack = [(0, -1, [])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target and res not in result:
                result.append(res)
            for i in range(start + 1, len(candidates)):
                t = total + candidates[i]
                if t > target:
                    break
                stack.append((t, i, res + [candidates[i]]))
        return result

s = Solution()
print s.combinationSum2([10,1,2,7,6,1,5], 8)