class Solution:
    def binaryGap(self, n: int) -> int:
        b = format(n,"b")
        max_gap = 0
        previous = -1
        for i,bit in enumerate(b):
            if bit == "1":
                if previous != -1:
                    max_gap = max(max_gap,i-previous)
                previous = i
        return max_gap



        