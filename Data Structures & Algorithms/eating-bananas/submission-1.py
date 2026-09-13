import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # find max # of bananas can eat in an hour
        max_n = max(piles)

        left = 1
        right = max_n

        cur_k = max_n

        while left <= right:
            k = (right - left) // 2 + left

            # calc total num of hours per pile
            total_h = 0
            for p_num in range(len(piles)):
                cur_h = math.ceil(piles[p_num] / k)
                total_h += cur_h
            
            # if num of hours less than h, and cur_k > k
            # if works, then smaller speed might work
            if total_h <= h and k < cur_k:
                cur_k = k

                right = k - 1
            else:
                left = k + 1
        
        return cur_k
