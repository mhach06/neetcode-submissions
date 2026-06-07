class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Will store tuples of (index, height)
        max_area = 0

        for idx, h in enumerate(heights):
            # We track where this current bar 'h' can start extending to the left.
            # By default, it starts at its own index.
            start_idx = idx
            
            # If the current bar is shorter than the bar on top of the stack,
            # the bar on top of the stack cannot extend any further to the right.
            while stack and stack[-1][1] > h:
                popped_idx, popped_h = stack.pop()
                
                # Calculate the area for the popped bar.
                # It can extend from its own start_idx up to (but not including) idx.
                cur_area = popped_h * (idx - popped_idx)
                max_area = max(max_area, cur_area)
                
                # Because the popped bar was taller than our current bar 'h',
                # 'h' can stretch backwards and occupy the popped bar's starting position.
                start_idx = popped_idx
            
            # Append the bar with its adjusted, furthest-left starting index
            stack.append((start_idx, h))
        
        # Cleanup: Any bars left in the stack can extend all the way 
        # to the very right end of the histogram (len(heights))
        while stack:
            popped_idx, popped_h = stack.pop()
            cur_area = popped_h * (len(heights) - popped_idx)
            max_area = max(max_area, cur_area)
        
        return max_area

            