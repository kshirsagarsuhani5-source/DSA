class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        best_x = 0
        best_y = 0
        max_quality = -1

        for x in range(51):
            for y in range(51):
                quality = 0

                for tx, ty, q in towers:
                    dx = x - tx
                    dy = y - ty

                    distance = (dx * dx + dy * dy) ** 0.5

                    if distance <= radius:
                        quality += int(q / (1 + distance))

                if quality > max_quality:
                    max_quality = quality
                    best_x = x
                    best_y = y

        return [best_x, best_y]