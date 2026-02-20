class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr=date.split("-")
        result  = []
        for i in range(len(arr)):
            temp=int(arr[i])
            result.append(format(temp,"b"))
        return "-".join(result)
        