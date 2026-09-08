class Solution:
    def countMaxOrSubsets(self, nums):
        max_or = 0

        for num in nums:
            max_or = max_or | num

        def backtrack(index, current_or):
            if index == len(nums):
                if current_or == max_or:
                    return 1
                return 0

            # Take the current number
            take = backtrack(
                index + 1,
                current_or | nums[index]
            )

            # Don't take the current number
            skip = backtrack(
                index + 1,
                current_or
            )

            return take + skip

        return backtrack(0, 0)