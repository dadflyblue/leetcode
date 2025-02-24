from typing import List

class Solution:
    """
    The problem link: <https://leetcode.com/problems/best-time-to-buy-and-sell-stock>

    **Constraints:**

    - `1 <= prices.length <= 10^5`
    - `0 <= prices[i] <= 10^4`

    **Problem:**

    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a 
    different day in the future to sell that stock. Return the maximum profit you can achieve 
    from this transaction. If you cannot achieve any profit, return 0.

    """

    def maxProfit(self, prices: List[int]) -> int:
        """
        **Implementation Notes:**

        It's easy to come up with a brute force solution in which it tries all pairs of 
        price and keep tracking the maximum profit of all comparations. However, the brute
        force solution needs O(N^2) time to find the final maximum profit. 
        
        For a quicker way, we can use a dynamic programming approach. Assuming that we've 
        already known a subarray's maximum profit and its minimum price, let's keep these
        two values in variables `m` and `b` respectively. Now if we add a new price `p` 
        in this array, the new maximum profit should be: `m = max(p-b, m)`, and the new 
        minimum price should be: `b = min(p, b)`; This way, we only need to walk through 
        the array once to obtain the final maximum profit.

        This implementation would be in linear O(N) time and O(1) space.

        **DocTest:**

        >>> s = Solution()

        >>> prices = [7,1,5,3,6,4]
        >>> s.maxProfit(prices)
        5

        >>> prices = [7,6,4,3,1]
        >>> s.maxProfit(prices)
        0
        """

        m, b = 0, prices[0]
        for p in prices[1:]:
            m = max(p-b, m)
            b = min(p, b)
        return m


    def maxProfitBruteForce(self, prices: List[int]) -> int:
        m = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                m = max(m, prices[j]-prices[i])
        return m


def _doctest():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()