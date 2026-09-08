class Solution(object):
    def checkEqualPartitions(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(nums)

        for mask in range(1, 1 << n):
            product = 1

            for i in range(n):
                if mask & (1 << i):
                    product *= nums[i]

            if product == target:
                other = 1

                for i in range(n):
                    if not (mask & (1 << i)):
                        other *= nums[i]

                if other == target:
                    return True

        return False