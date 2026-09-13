class TimeMap:

    def __init__(self):
        # Initialize a dictionary attached to 'self'
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key doesn't exist, create an empty list for it
        if key not in self.store:
            self.store[key] = []
        # assume timestamps are increasing automatically
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        left = 0
        right = len(self.store[key]) - 1

        cur_val = ""

        while left <= right:
            cur = ((right - left) // 2) + left
            cur_time = self.store[key][cur][0]

            if cur_time <= timestamp:
                left = cur + 1
                cur_val = self.store[key][cur][1]
            else:
                right = cur - 1
        
        return cur_val



        
