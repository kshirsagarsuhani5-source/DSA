class Solution(object):
    def maximumWidth(self, planks):
        """
        :type planks: List[int]
        :rtype: int
        """
        freq = {}

        for x in planks:
            freq[x] = freq.get(x, 0) + 1

        heights = list(freq.keys())
        count = {}

        # Original planks
        for x in heights:
            count[x] = freq[x]

        # Combine two planks
        for i in range(len(heights)):
            a = heights[i]

            # a + a
            h = a + a
            count[h] = count.get(h, 0) + freq[a] // 2

            # a + b, where a != b
            for j in range(i + 1, len(heights)):
                b = heights[j]

                h = a + b
                pairs = min(freq[a], freq[b])

                count[h] = count.get(h, 0) + pairs

        return max(count.values())