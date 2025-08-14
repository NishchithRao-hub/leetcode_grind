class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Works only for integers (O(nlogn), O(1))
        # low, high = 0, len(nums)-1
        # while low < high:
        #     mid = low + (high - low)//2
        #     countOfLess = sum(1 for num in nums if num <= mid)

        #     if countOfLess <= mid:
        #         low = mid+1
        #     else:
        #         high = mid

        # return high

        # Tortoise and Hare soln (Smart) (O(n), O(1))
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
