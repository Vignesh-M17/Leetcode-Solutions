class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        s = []
        a = 0
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                a += accounts[i][j]
            s.append(a)
            a = 0
        return max(s)