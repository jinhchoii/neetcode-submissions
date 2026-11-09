class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        number_set = set(nums)

        longest = 0

        for number in number_set:
            if number - 1 in number_set:
                continue

            current_number= number
            current_length = 1

            while current_number +1 in number_set:
                current_number += 1
                current_length += 1

            longest = max(longest,current_length)

        return longest