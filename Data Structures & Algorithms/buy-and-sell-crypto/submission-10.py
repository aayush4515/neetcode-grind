class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        res = 0
        left = 0
        right = 1

        while right < len(prices):
            # check if left >= right
            if prices[left] > prices[right]:
                # shift the left pointer all the way to the nexy possible minimum
                left = right
            else:
                profit = prices[right] - prices[left]
                res = max(res, profit)
            right += 1
        
        return res