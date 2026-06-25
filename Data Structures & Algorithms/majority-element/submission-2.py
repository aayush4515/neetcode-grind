class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # not the most optimal solution
        threshold = math.floor(len(nums) / 2)

        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        largest_val = max(sorted(list(freq_map.values())))

        for key, val in freq_map.items():
            if val == largest_val:
                return key