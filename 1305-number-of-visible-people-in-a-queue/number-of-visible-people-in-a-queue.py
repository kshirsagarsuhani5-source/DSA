class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        ans = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):

            while stack and heights[i] > stack[-1]:
                stack.pop()
                ans[i] += 1

            if stack:
                ans[i] += 1

            stack.append(heights[i])
        return ans