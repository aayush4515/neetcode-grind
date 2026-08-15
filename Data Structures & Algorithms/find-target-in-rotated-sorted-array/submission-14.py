class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # multiple cases

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if target == nums[middle]:
                return middle

            # if the middle is in the left sorted portion
            if nums[middle] >= nums[left]:
                # if the target is less than the middle
                if target < nums[middle]:
                    if target < nums[left]:
                        # search right
                        left = middle + 1
                    else:
                        # search left
                        right = middle - 1
                # if the target is greater than the middle
                else:
                    # search right
                    left = middle + 1
            # if the middle is in the right sorted portion
            else:
                if target > nums[middle]:
                    if target > nums[right]:
                        right = middle - 1
                    else:
                        left = middle + 1
                else:
                    right = middle - 1

        return -1
