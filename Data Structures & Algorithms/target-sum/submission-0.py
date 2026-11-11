class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways = {0: 1}

        # Process each number once, stopping after the final number.
        for number in nums:
            # Collect counts after assigning this number a sign.
            next_ways = {}

            # Extend every sum reachable before this number.
            for current_sum, count in ways.items():
                # Add all these assignments using a plus sign.
                next_ways[current_sum + number] = next_ways.get(current_sum + number, 0) + count
                # Add all these assignments using a minus sign.
                next_ways[current_sum - number] = next_ways.get(current_sum - number, 0) + count

            # Use the completed counts for the next number.
            ways = next_ways

        # Return the target's count, or zero if it was never reached.
        return ways.get(target, 0)