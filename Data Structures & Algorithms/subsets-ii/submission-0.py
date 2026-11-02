class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []

        nums.sort()

        def dfs(i):

            if i == len(nums):
                if path not in result:
                    result.append(path.copy())
                return

            path.append(nums[i])
            dfs(i+1)
            path.pop()
            dfs(i+1)

        dfs(0)

        return result    