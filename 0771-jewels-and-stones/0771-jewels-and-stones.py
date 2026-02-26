class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for char in jewels:
            for schar in stones:
                if char == schar:
                    count+=1
        return count
        