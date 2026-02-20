class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        l = len(nums)
        odd_result = 0
        even_result = 0
        for i in range(l):
            if i % 2 == 0:
                even_result += nums[i]
            else:
                odd_result += nums[i]
        return even_result-odd_result