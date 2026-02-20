class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        rev = s[:k][::-1]+s[k:]
        return rev
        