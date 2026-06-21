class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = []
        fact = 1
        
        for i in range(1, n + 1):
            numbers.append(str(i))
            fact *= i
        
        k -= 1
        ans = ""
        
        for i in range(n, 0, -1):
            fact //= i
            index = k // fact
            ans += numbers.pop(index)
            k %= fact
        
        return ans
        