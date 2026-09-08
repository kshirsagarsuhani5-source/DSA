class Solution:
    def countQuadruplets(self, nums):
        n = len(nums)
        ans = 0
        dp = [0] * n

        for j in range(n):
            greater = 0

            for k in range(n - 1, j, -1):

                if nums[k] < nums[j]:
                    ans += dp[k] * greater
                else:
                    greater += 1
                    dp[k] += 1

        return ans