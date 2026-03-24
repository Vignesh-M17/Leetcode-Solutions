class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        result = []
        for num in nums:
            result.append(sum+num)
            sum+=num
        return result        