class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Hash Table soln
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            result[tuple(count)].append(s)

        return list(result.values())

        #Time complexity = O(m * nlogn)
        #Space complexity = O(m*n) -> output, O(m) extra space

        # Sorting and storing in hash map
        # result = defaultdict(list)
        # for s in strs:
        #     sortedS = "".join(sorted(s))
        #     result[sortedS].append(s)
        # return list(result.values())
        
        #Time complexity = O(m * nlogn)
        #Space complexity = O(m*n)
        #Where m is the number of strings, n is the length of the longest string.
        

        
