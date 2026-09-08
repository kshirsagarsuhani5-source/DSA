class Solution(object):
    def maximumGood(self, statements):
        """
        :type statements: List[List[int]]
        :rtype: int
        """
        n = len(statements)
        ans = 0

        for mask in range(1 << n):
            valid = True
            good = 0

            for i in range(n):
                if mask & (1 << i):
                    good += 1

                    for j in range(n):
                        if statements[i][j] == 1:
                            if not (mask & (1 << j)):
                                valid = False
                                break

                        elif statements[i][j] == 0:
                            if mask & (1 << j):
                                valid = False
                                break

                    if not valid:
                        break

            if valid:
                ans = max(ans, good)

        return ans