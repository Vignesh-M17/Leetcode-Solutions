class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for k in operations:
            if k == "X++" or k == "++X":
                count+=1
            elif k == "X--" or k == "--X":
                count-=1
        return count

        