class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        temp = []
        for num in nums:
            if num >= k:
                temp.append(num)
        return len(nums)-len(temp)
        