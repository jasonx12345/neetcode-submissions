class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #buy on one day sell on another day, we want to max the profit
        # max profit is just buy on the min day, and and any day after it
        # you always want your left pointer to be less than you right pointer
        # you update the left pointer if its a negative profit
        # we update theright pointer if the new difference is bigger than the current profit
        left = 0
        right = 1
        maxProfit = 0
        while right < len(prices):
            #profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices [left]
                #updated it if new profit greater than existing 
                maxProfit = max(maxProfit, profit)
            #otherwise keep going
            else:
                left = right
            #shift right
            right += 1
        return maxProfit
        