class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pointer_zero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pointer_zero],nums[i]=nums[i],nums[pointer_zero]
                pointer_zero+=1
        print(nums)