class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            return [nums.index(target), len(nums) - 1 - sorted(nums, reverse=True).index(target)]
        except Exception as e:
            return [-1, -1]