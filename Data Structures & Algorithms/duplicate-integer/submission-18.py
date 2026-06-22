class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        if len(nums) > len(temp):
            return True
        return False