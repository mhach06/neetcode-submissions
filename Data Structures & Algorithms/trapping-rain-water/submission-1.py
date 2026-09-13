from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # This will store indices, not tuples
        area = 0
        
        for idx, h in enumerate(height):
            # While the current bar is taller than the bar at the top of the stack,
            # we have a potential right wall trapping water.
            while stack and h > height[stack[-1]]:
                top_of_stack = stack.pop()  # The bottom of our current pool layer
                
                # If stack becomes empty, there's no left wall to hold water
                if not stack:
                    break
                
                left_idx = stack[-1]
                
                # Calculate the bounded dimensions of this horizontal layer
                width = idx - left_idx - 1
                bounded_height = min(height[left_idx], h) - height[top_of_stack]
                
                area += width * bounded_height
            
            # Push the current index onto the stack
            stack.append(idx)
            
        return area
            
            