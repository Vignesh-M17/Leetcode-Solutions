class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        temp = []
        for i in range(len(order)):
            for j in range(len(friends)):
                if order[i] == friends[j]:
                    temp.append(friends[j])
        return temp
        