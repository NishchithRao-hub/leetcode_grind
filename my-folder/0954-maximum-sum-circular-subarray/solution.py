class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Kadane's and Inverse Kadane solution
        globalMax, globalMin = nums[0], nums[0]
        currMax, currMin = 0, 0
        total = 0

        for num in nums:
            currMax = max(currMax + num, num)
            currMin = min(currMin + num, num)
            total += num
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)

        if globalMax > 0:
            return max(globalMax, total - globalMin)
        else:
            return globalMax
        
