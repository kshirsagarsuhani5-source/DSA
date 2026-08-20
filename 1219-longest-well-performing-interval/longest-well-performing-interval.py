class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        first = {}
        score = 0
        ans = 0

        for i, h in enumerate(hours):
            if h > 8:
                score += 1
            else:
                score -= 1

            if score > 0:
                ans = i + 1

            if score not in first:
                first[score] = i

            if score - 1 in first:
                ans = max(ans, i - first[score - 1])
        return ans
        