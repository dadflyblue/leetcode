from typing import List

class Solution:
    """
    The problem link: <https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii>

    **Constraints:**

    - `1 <= prices.length <= 3 * 10^4`
    - `0 <= prices[i] <= 10^4`

    **Problem:**

    You are given an integer array prices where prices[i] is the price of a given stock 
    on the ith day. On each day, you may decide to buy and/or sell the stock. You can 
    only hold at most one share of the stock at any time. However, you can buy it then 
    immediately sell it on the same day. Find and return the maximum profit you can achieve.

    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        **Implementation Notes:**

        The test case `prices = [1,2,3,4,5]` gives us a very helpful hint; It tells us that 
        the maximum profit can be achieved either by buying at 1 and selling at 5, or by 
        buying at 1 and selling at 2 and then buying at 2 and selling at 3, and repeating this 
        process all the way to selling at 5.
        
        It can be easily proved in an array if there is a maximum profit by buying at `i` and 
        selling at `j`, and if there's a price `k` located between `i` and `j` which is greater 
        than `i` and lower than `j`, the maximum profit can also be achieved by buying at `i` 
        and selling at `k` and then buying at `k` and selling at j, because:
         
        `j - i = (k - i) + (j - k)`.

        Based on above observation, Assuming that we've already known the maximum profit in a 
        subarray is `m` and the last price is `b`, when we add a new price `p` to this array, the
        new maximum profit should be: `m += (p - b) if (p > b) else 0`

        This implementation would be in linear O(N) time and O(1) space.
        
        **DocTest:**

        >>> s = Solution()

        >>> prices = [7,1,5,3,6,4]
        >>> s.maxProfit(prices)
        7

        >>> prices = [1,2,3,4,5]
        >>> s.maxProfit(prices)
        4

        >>> prices = [7,6,4,3,1]
        >>> s.maxProfit(prices)
        0
        """

        b, m = prices[0], 0
        for p in prices[1:]:
            m += (p - b) if (p > b) else 0
            b = p
        return m


def _doctest():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()