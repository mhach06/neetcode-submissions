class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            cur = left + ((right - left) // 2)

            if nums[cur] == target:
                return cur
            
            if nums[left] <= nums[cur]:
                if nums[left] <= target <= nums[cur]:
                    right = cur - 1
                else:
                    left = cur + 1
            
            else:
                if nums[cur] <= target <= nums[right]:
                    left = cur + 1
                else:
                    right = cur - 1

        return -1