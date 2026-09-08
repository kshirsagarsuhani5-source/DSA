class Solution(object):
    def maximumRequests(self, n, requests):
        """
        :type n: int
        :type requests: List[List[int]]
        :rtype: int
        """
        m = len(requests)
        ans = 0

        for mask in range(1 << m):
            count = 0
            balance = [0] * n

            for i in range(m):
                if mask & (1 << i):
                    count += 1
                    a = requests[i][0]
                    b = requests[i][1]
                    balance[a] -= 1
                    balance[b] += 1

            if all(x == 0 for x in balance):
                ans = max(ans, count)

        return ans