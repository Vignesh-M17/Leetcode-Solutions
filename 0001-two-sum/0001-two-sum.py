class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        j = 1
        for i in range(l):
            for j in range(i+1,l):
                if nums[i]+nums[j]==target:
                    return [i,j]
        