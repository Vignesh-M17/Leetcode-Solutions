class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = ""
        st = (s.split(" "))
        for i in range(k):
            if i == k-1:
                result+=st[i]
            else:
                result+=st[i]+" "
        return result