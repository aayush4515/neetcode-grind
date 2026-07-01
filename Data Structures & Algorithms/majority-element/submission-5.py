class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # not the most optimal solution
        # using a frequency map

        '''
        threshold = math.floor(len(nums) / 2)

        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        largest_val = max(sorted(list(freq_map.values())))

        for key, val in freq_map.items():
            if val == largest_val:
                return key
        '''

        # trying to optimize this for O(1) space using Boyer-Moore's Algorithm
        res = None      # res acts as prev
        count = 0

        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1
        
        return res

        


              