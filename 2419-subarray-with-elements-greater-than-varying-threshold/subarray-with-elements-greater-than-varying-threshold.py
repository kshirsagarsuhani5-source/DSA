class Solution(object):
    def validSubarraySize(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        n = len(nums)
        stack = []

        for i in range(n + 1):
            curr = nums[i] if i < n else 0

            while stack and nums[stack[-1]] >= curr:
                j = stack.pop()

                left = stack[-1] if stack else -1
                right = i

                length = right - left - 1

                if nums[j] * length > threshold:
                    return length

            stack.append(i)
        return -1