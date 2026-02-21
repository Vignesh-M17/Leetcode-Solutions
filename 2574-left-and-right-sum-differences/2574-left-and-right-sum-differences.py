class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        result = []
        for x in nums:
            right-=x
            result.append(abs(left-right))
            left+=x
        return result

