class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        const = x
        counter = 1

        while counter < abs(-n):
            x *= const
            counter += 1
        
        if n < 0:
            return 1/x
        else:
            return x
    
        
        