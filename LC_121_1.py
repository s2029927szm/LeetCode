#runtime complexity is O(n), space complexity is O(1), n is the length of list

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        pmax=0
        for i in range(1, len(prices)):
            if prices[i]<min:
                min=prices[i]
            else:
                pmax=max(pmax, prices[i]-min)
        return pmax