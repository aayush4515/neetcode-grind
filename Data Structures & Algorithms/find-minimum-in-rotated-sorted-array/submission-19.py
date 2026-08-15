class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        res = nums[0]

        while left <= right:
            middle = left + (right - left) // 2
            res = min(res, nums[middle])

            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break
                
            if nums[middle] >= nums[left]:
                # search right
                left = middle + 1
            else:
                # search left
                right = middle - 1
        
        return res

