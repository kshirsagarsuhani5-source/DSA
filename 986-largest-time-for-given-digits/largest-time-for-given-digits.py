class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        import itertools

        ans = ""

        for p in itertools.permutations(arr):
            hour = p[0] * 10 + p[1]
            minute = p[2] * 10 + p[3]

            if hour < 24 and minute < 60:
                h = str(hour)
                m = str(minute)

                if hour < 10:
                    h = "0" + h

                if minute < 10:
                    m = "0" + m

                current = h + ":" + m

                if current > ans:
                    ans = current

        return ans