class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)

        # As long as there's at least one unexamined element between left and right
        while left + 1 < right:
            # Calculate the true midpoint of the current window
            cur = left + (right - left) // 2
            
            if nums[cur] == target:
                return cur
            
            if nums[cur] < target:
                left = cur   # Narrow window to the right half
            else:
                right = cur  # Narrow window to the left half
            
        return -1
