class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums: 
            return 0

        if len(nums) == 1:
            return nums[0]

        def rob_linear(start, end):
            previous_two = 0
            previous_one = 0

            for index in range(start,end+1):

                rob_current = previous_two + nums[index]
                skip_current = previous_one

                current_best = max(rob_current, skip_current)

                previous_two = previous_one
                previous_one = current_best

            return previous_one

        exclude_last = rob_linear(0,len(nums)-2)
        exclude_first = rob_linear(1,len(nums)-1)

        return max(exclude_last, exclude_first)