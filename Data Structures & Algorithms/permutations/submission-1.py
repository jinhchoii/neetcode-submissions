class Solution:
    def permute(self, nums):
        if len(nums) == 0:
            return []

        result = []
        path = []

        def dfs():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for num in nums:
                if num in path:
                    continue

                path.append(num)
                dfs()
                path.pop()

        dfs()
        return result