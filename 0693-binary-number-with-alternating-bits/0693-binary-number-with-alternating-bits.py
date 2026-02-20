class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)
        count = 0
        for i in range(len(b)-1):
            if(b[i]!=b[i+1]):
                count+=1
            else:
                count-=1
        if count==(len(b)-1):
            return True
        else:
            return False      