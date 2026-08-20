class Solution(object):
    def countGoodSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        left = [-1] * n
        stack = []

        for i, x in enumerate(nums):
            while (
                stack
                and nums[stack[-1]] < x
                and (nums[stack[-1]] | x) == x
            ):
                stack.pop()

            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and (nums[stack[-1]] | nums[i]) == nums[i]:
                stack.pop()

            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0

        for i in range(n):
            ans += (i - left[i]) * (right[i] - i)

        return ans