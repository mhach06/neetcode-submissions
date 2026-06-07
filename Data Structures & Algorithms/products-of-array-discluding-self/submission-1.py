class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [1] * n
        suffixes = [1] * n
        
        # Fill prefixes (Left to Right)
        prefix_product = 1
        for i in range(n):
            prefixes[i] = prefix_product
            prefix_product *= nums[i]
            
        # Fill suffixes (Right to Left)
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            suffixes[i] = suffix_product
            suffix_product *= nums[i]
            
        # Combine them
        final_list = []
        for i in range(n):
            final_list.append(prefixes[i] * suffixes[i])
            
        return final_list

            

