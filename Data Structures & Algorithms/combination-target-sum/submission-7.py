class Solution:
    def combinationSum(self, candidates, target):
        result = []
        path = []

        def dfs(index):
            if sum(path) == target:
                result.append(path.copy())
                return

            if sum(path) > target:
                return

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                dfs(i)
                path.pop()

        dfs(0)
        return result