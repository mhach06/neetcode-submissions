class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left < right:
            cur = ((right - left) // 2) + left

            if nums[right] < nums[cur]:
                left = cur + 1
            else:
                right = cur
        
        return nums[left]

        