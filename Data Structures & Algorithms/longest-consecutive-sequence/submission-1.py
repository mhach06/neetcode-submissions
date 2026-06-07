class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        arr = set()

        max = 1

        for num in nums:
            arr.add(num)
        
        for num in arr:
            longest = 1
            while (num - 1 in arr):
                longest += 1
                num -= 1
            
            if longest > max:
                max = longest

        return max
            

        