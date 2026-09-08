class Solution:
    def maxStrength(self, nums):
        if len(nums) == 1:
            return nums[0]

        positive = []
        negative = []
        zero = False

        for num in nums:
            if num > 0:
                positive.append(num)
            elif num < 0:
                negative.append(num)
            else:
                zero = True

        product = 1

        # Take all positive numbers
        for num in positive:
            product *= num

        # If odd number of negatives, remove the one
        # closest to zero
        negative.sort()

        if len(negative) % 2 == 1:
            negative.pop()

        # Multiply remaining negative pairs
        for num in negative:
            product *= num

        # If we have at least one positive or a pair of negatives
        if positive or negative:
            return product

        # Only zeros are left
        return 0