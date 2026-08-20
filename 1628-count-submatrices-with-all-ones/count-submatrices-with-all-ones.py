class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        rows = len(mat)
        cols = len(mat[0])

        heights = [0] * cols
        ans = 0

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 1:
                    heights[c] += 1
                else:
                    heights[c] = 0

            stack = []
            count = [0] * cols

            for c in range(cols):
                while stack and heights[stack[-1]] >= heights[c]:
                    stack.pop()

                if stack:
                    prev = stack[-1]
                    count[c] = count[prev] + heights[c] * (c - prev)
                else:
                    count[c] = heights[c] * (c + 1)

                ans += count[c]
                stack.append(c)

        return ans