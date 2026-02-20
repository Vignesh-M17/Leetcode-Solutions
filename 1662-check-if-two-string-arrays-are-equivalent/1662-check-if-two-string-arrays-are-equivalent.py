class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=""
        s2=""
        for word in word1:
            s1+=word
        for sword in word2:
            s2+=sword
        return s1==s2