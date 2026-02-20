class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = len(nums)
        temp = []
        l_temp = []
        r_temp = []
        for i in range (l-n):
            l_temp.append(nums[i])
        for i in range(n,l):
            r_temp.append(nums[i])
        for i in range(l-n):
            temp.append(l_temp[i])
            temp.append(r_temp[i]) 
        return temp
