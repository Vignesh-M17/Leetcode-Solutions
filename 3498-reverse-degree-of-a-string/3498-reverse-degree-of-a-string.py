class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += (26-(ord(s[i].lower())-ord('a')))*(i+1)
        return result