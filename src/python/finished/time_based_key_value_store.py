# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap:

    def __init__(self):
        self.key_to_timestamps_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Initialize the timestamp array if not initialized
        if not key in self.key_to_timestamps_dict:
            self.key_to_timestamps_dict[key] = []

        self.key_to_timestamps_dict[key].append((timestamp, value))
        return None

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_to_timestamps_dict:
            return ""
        
        if len(self.key_to_timestamps_dict[key]) == 0:
            return ""
        
        timestamps = self.key_to_timestamps_dict[key]
        
        low = 0
        high = len(timestamps) - 1

        if timestamp < timestamps[low][0]:
            return ""

        # timestamp is within range
        while low < high:
            mid = (high - low) // 2 + low

            if timestamps[mid][0] == timestamp:
                return timestamps[mid][1]
            elif timestamps[mid][0] < timestamp:
                low = mid + 1
            else:
                high = mid - 1

        if timestamps[low][0] <= timestamp:
           return timestamps[low][1]
        
        return timestamps[low-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
