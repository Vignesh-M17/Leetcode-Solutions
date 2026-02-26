class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        count = 0
        temp = []
        for string in sentences:
            for word in string:
                if word.isalpha():
                    pass
                elif word.isspace():
                    count+=1
            temp.append(count+1)
            count = 0
        return max(temp)