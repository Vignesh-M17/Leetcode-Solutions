class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums,target,is_left):
            left,right = 0,len(nums)-1
            idx = -1

            while(left<=right):
                mid  = (left+right)//2
                mid_number = nums[mid]

                if mid_number<target:
                    left = mid+1
                elif mid_number>target:
                    right= mid-1
                else:
                    idx = mid
                    if is_left:
                        right = mid-1
                    else:
                        left=mid+1
            return idx
        left = binary_search(nums,target,True)
        right = binary_search(nums,target,False)
        return [left,right]

        