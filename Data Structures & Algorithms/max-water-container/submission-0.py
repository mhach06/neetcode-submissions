class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width = right - left (for every run)
        # area = width * min(heights[left], heights[right])
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            area = h * w

            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
        
        return max_area

        
