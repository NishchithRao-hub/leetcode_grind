class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort solution
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        result = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result

# Time complexity = O(n)
# Space complexity = O(n)

        # Sorting solution
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr.sort()

        # result = []
        # while len(result) < k:
        #     result.append(arr.pop()[1])
        # return result

# Time complexity = O(n log n)
# Space complexity = O(n)

        
