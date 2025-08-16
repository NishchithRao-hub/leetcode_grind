class TimeMap(object):
    # Binary search method with array
    def __init__(self):
        self.keyValueStore = {}


    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.keyValueStore:
            self.keyValueStore[key] = []
        self.keyValueStore[key].append([value, timestamp])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        result, values = "", self.keyValueStore.get(key, [])
        left, right = 0, len(values)-1
        while left <= right:
            mid = (right+left)//2
            if values[mid][1] <= timestamp:
                result = values[mid][0]
                left = mid+1
            else:
                right = mid-1

        return result

# Time - O(1) -> set, O(log n)-> get;
# Space - O(m*n) -> n is num of values for m num of keys
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
