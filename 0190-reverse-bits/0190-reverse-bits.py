class Solution:
    def reverseBits(self, n: int) -> int:
        padded = format(n,"032b")
        reverse_p = padded[::-1]
        result = int(reverse_p,2)
        return result

        