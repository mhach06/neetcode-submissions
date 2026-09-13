class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Always run binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total_len = m + n
        
        # The total number of elements that should be in the left half
        half_len = (total_len + 1) // 2 
        
        # Binary search bounds for the partition line in nums1
        left, right = 0, m
        
        while left <= right:
            # i is the partition line in nums1
            # j is the partition line in nums2
            i = (left + right) // 2
            j = half_len - i
            
            # Find the edge points around the lines. 
            # Use negative/positive infinity if the line is at the absolute edge of an array.
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Cross-compare to see if we found the perfect cut
            if left1 <= right2 and left2 <= right1:
                # We found the correct partition!
                # If the total number of elements is odd, the median is just the max of the left side.
                if total_len % 2 != 0:
                    return max(left1, left2)
                # If even, it's the average of the max of the left side and the min of the right side.
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                
            # If the left side of nums1 is too big, move the line left
            elif left1 > right2:
                right = i - 1
            # If the left side of nums2 is too big, move the line in nums1 right
            else:
                left = i + 1

