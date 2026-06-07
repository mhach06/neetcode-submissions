class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []

        for pos, spd in cars:
            # 2. Calculate the time it takes this car to reach the target alone
            time_to_target = (target - pos) / spd
            
            # 3. Push to stack
            stack.append(time_to_target)
            
            # 4. If the car behind (stack[-1]) arrives FASTER or at the SAME TIME 
            # as the car ahead of it (stack[-2]), they merge into one fleet.
            # We pop the faster car because it adopts the slower speed of the fleet ahead.
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        # The remaining items in the stack represent the distinct fleets
        return len(stack)