class Solution(object):
    def longestAlternating(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        left_less = [1] * n
        left_greater = [1] * n

        right_less = [1] * n
        right_greater = [1] * n

        ans = 1

        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                left_less[i] = left_greater[i - 1] + 1

            elif nums[i - 1] > nums[i]:
                left_greater[i] = left_less[i - 1] + 1

            ans = max(ans, left_less[i], left_greater[i])

        # Alternating subarray starting at i
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                right_less[i] = right_greater[i + 1] + 1

            elif nums[i] > nums[i + 1]:
                right_greater[i] = right_less[i + 1] + 1

        # Remove nums[i]
        for i in range(1, n - 1):

            if nums[i - 1] < nums[i + 1]:
                ans = max(
                    ans,
                    left_greater[i - 1] + right_greater[i + 1]
                )

            elif nums[i - 1] > nums[i + 1]:
                ans = max(
                    ans,
                    left_less[i - 1] + right_less[i + 1]
                )

        return ans