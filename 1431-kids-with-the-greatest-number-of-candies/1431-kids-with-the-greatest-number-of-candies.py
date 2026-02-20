class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        l = len(candies)
        temp = []
        f = 0 
        for i in range(l):
            f = candies[i]
            f += extraCandies
            if f >= m:
                temp.append(bool(1))
            else:
                temp.append(bool(0))
        return temp
