class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1
        
        prev = 1.0/n                    # Passenger 2
        
        for i in range(1, n-1):         # Passenger i
            prev *= (1.0 + 1.0/(n-i))
            
        return (1-prev) 
        