class Solution:
    def search(self, nums: List[int], target: int) -> int:

        cur = int(len(nums) / 2)

        left = -1
        right = len(nums)

        while cur > left and cur < right:
            if nums[cur] == target:
                return cur
            
            if nums[cur] < target:
                left = cur
                cur += int((right - left) / 2)
            
            elif nums[cur] > target:
                right = cur
                cur -= int((cur - left) / 2)
            
        return -1
