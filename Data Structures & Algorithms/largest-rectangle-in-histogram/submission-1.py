class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        if len(heights) == 1:
            return heights[0]

        stack = []
        max_area = 0
        width = 0

        cur_min = heights[0]

        for h in heights:

            if stack:
                # do stuff
                stack.append(h)
                width = 1
                counter = len(stack) - 1
                cur_min = h
                
                while counter >= 0:
                    
                    cur_min = min(cur_min, stack[counter])
                    cur_area = width * cur_min

                    max_area = max(max_area, cur_area)
                    
                    counter -= 1
                    width += 1

            else:
                max_area = h
                stack.append(h)
        
        return max_area