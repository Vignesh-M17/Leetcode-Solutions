class Solution:
    def concatenatedBinary(self, n: int) -> int:
        l = n+1
        res =""
        for i in range(1,l):
            res+=(bin(i)[2:])
        result = int(res,2)
        if result > pow(10,5):
            result = result%1000000007
        return result    