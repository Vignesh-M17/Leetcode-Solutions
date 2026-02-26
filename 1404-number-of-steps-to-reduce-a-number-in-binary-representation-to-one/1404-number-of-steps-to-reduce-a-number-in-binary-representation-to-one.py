class Solution:
    def numSteps(self, s: str) -> int:
        t = (int(s,2))
        count = 0
        while(t!=1):
            if t%2!=0:
                t=t+1
                count+=1
            else:
                t=t//2
                count+=1
        return count


        