class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isprime(n):
            if n<=1:
                return False
            else:
                for i in range(2,int(math.sqrt(n))+1):
                    if n%i==0:
                        return False
                return True
        count  = 0
        prime = 0
        for i in range(left,right+1):
            b = format(i,"b")
            for j in range(len(b)):
                if b[j]=="1":
                    count+=1
                else:
                    continue
            if isprime(count):
                count = 0
                prime+=1
            else:
                count = 0
        return prime
   