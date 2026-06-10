class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return abs(a)

        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = {}

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0:
                    slope = (1, 0)      # vertical line
                elif dy == 0:
                    slope = (0, 1)      # horizontal line
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    if dx < 0:
                        dx = -dx
                        dy = -dy

                    slope = (dy, dx)

                slopes[slope] = slopes.get(slope, 0) + 1

            ans = max(ans, max(slopes.values()) + 1 if slopes else 1)

        return ans