class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dif = {}
        
        for index, num in enumerate(nums):
            if num in seen_dif:
                return [seen_dif[num], index]
            
            dif = target - num
            seen_dif[dif] = index

        return [None, None]
