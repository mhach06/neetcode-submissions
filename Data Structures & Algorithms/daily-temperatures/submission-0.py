class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # This will store indices, not the temperatures themselves

        for current_day, current_temp in enumerate(temperatures):
            # Check if the current day is warmer than the day on top of our stack
            while stack and temperatures[stack[-1]] < current_temp:
                prev_day = stack.pop()
                # The number of days to wait is the difference between indices
                result[prev_day] = current_day - prev_day
            
            # Always push the current day's index onto the stack
            stack.append(current_day)
        
        return result
