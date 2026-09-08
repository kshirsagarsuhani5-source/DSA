class Solution(object):
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = s[1:-1]
        ans = []

        # Generate all valid numbers from a string
        def get_numbers(x):
            res = []

            # Integer number
            if x == "0" or not x.startswith("0"):
                res.append(x)

            # Decimal numbers
            for i in range(1, len(x)):
                left = x[:i]
                right = x[i:]

                # Left side cannot have leading zero
                if len(left) > 1 and left[0] == "0":
                    continue

                # Right side cannot end with zero
                if right[-1] == "0":
                    continue

                res.append(left + "." + right)

            return res

        # Split string into x and y
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]

            x_values = get_numbers(left)
            y_values = get_numbers(right)

            for x in x_values:
                for y in y_values:
                    ans.append("(" + x + ", " + y + ")")

        return ans