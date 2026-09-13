class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect the cycle
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]          # 1 step: slow = slow.next
            fast = nums[nums[fast]]    # 2 steps: fast = fast.next.next
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle (the duplicate)
        slow = nums[0]                 # Reset slow to the start
        while slow != fast:
            slow = nums[slow]          # 1 step
            fast = nums[fast]          # 1 step (fast moves at slow's pace now)

        return slow
        