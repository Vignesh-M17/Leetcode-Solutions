class Solution:
    def scoreOfString(self, s: str) -> int:
        temp = []
        total = []
        for k in s:
            temp.append(ord(k))
        for i in range(len(temp)-1):
            total.append(abs(temp[i]-temp[i+1]))
        return sum(total)
        