class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0

        while left <= right:
            print(f"Count: {count}")
            if nums[left] == val:
                if nums[right] != val:
                    temp = nums[right]
                    nums[right] = nums[left]
                    nums[left] = temp
                    right -= 1
                else:
                    count += 1
                    right -= 1
                    continue
                count += 1
            left += 1
        return len(nums) - count