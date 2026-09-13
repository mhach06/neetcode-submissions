class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = nums.sort()
        result = []

        # [-4, -1, -1, 0, 1, 2]

        left = 1
        right = len(nums) - 1

        for fix in range(len(nums)):
            if fix != 0 and nums[fix] == nums[fix - 1]:
                continue

            left = fix + 1
            right = len(nums) - 1
            while left < right:

                sum = nums[fix] + nums[left] + nums[right]

                if sum == 0:
                    valid = [nums[fix], nums[left], nums[right]]
                    result.append(valid)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                if sum < 0:
                    left += 1
                
                if sum > 0:
                    right -= 1
        
        return result