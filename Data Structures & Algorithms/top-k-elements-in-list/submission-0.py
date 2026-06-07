import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        # get counts for each number
        for num in nums:
            if num in counts:
                counts[num] += 1
                continue
            
            counts[num] = 1
        
        max_heap = []
        for num, frequency in counts.items():
            heapq.heappush(max_heap, (-frequency, num))
        
        final_list = []
        for i in range(k):
            popped_tuple = heapq.heappop(max_heap)
            final_list.append(popped_tuple[1])
        
        return final_list
        
        