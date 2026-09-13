class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_list = nums.sort()
        result = []

        # [-4, -1, -1, 0, 1, 2]

        left = 1
        right = len(nums) - 1

        for fix in range(len(nums)):
            left = 1 if fix == 0 else 0
            right = len(nums) - 1
            while left < right:
                
                if left == fix:
                    left += 1
                    continue
                
                elif right == fix:
                    right -= 1
                    continue

                sum = nums[fix] + nums[left] + nums[right]

                if sum == 0:
                    if sorted([nums[fix], nums[left], nums[right]]) not in result:
                        valid = sorted([nums[fix], nums[left], nums[right]])
                        result.append([nums[fix], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                if sum < 0:
                    left += 1
                
                if sum > 0:
                    right -= 1
        
        return result