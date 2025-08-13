class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        target = newInterval[0]
        start, end = 0, len(intervals) - 1

        while start <= end:
            mid = (start + end) // 2
            if intervals[mid][0] < target:
                start = mid + 1
            else:
                end = mid - 1
        intervals.insert(start, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
        
