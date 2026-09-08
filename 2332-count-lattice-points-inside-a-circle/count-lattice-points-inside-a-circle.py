class Solution(object):
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        points = set()

        for x, y, r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):

                    dx = i - x
                    dy = j - y

                    if dx * dx + dy * dy <= r * r:
                        points.add((i, j))

        return len(points)  