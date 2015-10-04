class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = [i for i in range(1, 10)]
        target = n

        stack = [(0, -1, [])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target and len(res) == k:
                result.append(res)
            for i in range(start + 1, len(candidates)):
                t = total + candidates[i]
                if t > target:
                    break
                stack.append((t, i, res + [candidates[i]]))
        return result

s = Solution()
print s.combinationSum3(3, 9)