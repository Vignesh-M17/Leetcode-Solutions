class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        result = 0
        for i,char in enumerate(s):
            for j,schar in enumerate(t):
                if char == schar:
                    result+=abs(i-j)
        return result
        