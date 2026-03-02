class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res = ""
        if ch not in word:return word
        for i,char in  enumerate(word):
            if char == ch:
                res+=word[:i+1][::-1]
                res+=word[i+1:]
                break
        return res      