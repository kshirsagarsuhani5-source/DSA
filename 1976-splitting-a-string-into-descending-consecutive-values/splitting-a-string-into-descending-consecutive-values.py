class Solution(object):
    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def backtrack(index, prev, count):
            if index == len(s):
                return count >= 2

            num = 0

            for i in range(index, len(s)):
                num = num * 10 + int(s[i])

                # We need the next number to be exactly prev - 1
                if num >= prev:
                    continue

                if num == prev - 1:
                    if backtrack(i + 1, num, count + 1):
                        return True

            return False

        # Try every possible first number
        for i in range(1, len(s)):
            first = int(s[:i])

            if backtrack(i, first, 1):
                return True

        return False  