class Solution:
    def maxFreqSum(self, s: str) -> int:
        temp_v = []
        temp_c = []
        vowels = ['a','e','i','o','u']
        for i in range(len(s)):
            for j,t in enumerate(vowels):
                if vowels[j] == s[i]:
                    temp_v.append(s.count(vowels[j]))
                elif s[i] not in vowels:
                    temp_c.append(s.count(s[i]))
        u = max(temp_v,default=0)
        v = max(temp_c,default=0)
        return u+v          
        