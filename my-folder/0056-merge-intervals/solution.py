class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # intervals.sort(key=lambda pair:pair[0])
        # output = [intervals[0]]
        # for start, end in intervals:
        #     lastEnd = output[-1][1]
        #     if start <= lastEnd:
        #         output[-1][1] = max(lastEnd, end)
        #     else:
        #         output.append([start, end])
        # return output

        max_val = max(interval[0] for interval in intervals)
        mp = [0] * (max_val+1)
        for start, end in intervals:
            mp[start] = max(end+1, mp[start])

        interval_start = -1
        have = -1
        result = []
        for i in range(len(mp)):
            if mp[i] != 0:
                if interval_start == -1:
                    interval_start = i

                have = max(mp[i]-1, have)

            if have == i:
                result.append([interval_start, have])
                have = -1
                interval_start = -1

        if interval_start != -1:
            result.append([interval_start, have])

        return result




        
