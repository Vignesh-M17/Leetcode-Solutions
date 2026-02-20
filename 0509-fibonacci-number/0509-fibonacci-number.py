class Solution:
    def fib(self, n: int) -> int:
        x = 0
        y = 1
        i = 0
        while(i<n):
            x,y=y,x+y
            i+=1
        return x


        