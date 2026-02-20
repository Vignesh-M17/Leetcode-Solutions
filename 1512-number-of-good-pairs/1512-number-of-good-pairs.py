class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l = len(nums)
        count = 0
        for i in range(l):
            for j in range(l):
                if nums[i] == nums[j] and i < j:
                    count = count + 1
        return count
        