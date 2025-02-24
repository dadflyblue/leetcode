from typing import List

class Solution:
    """
    The problem link: <https://leetcode.com/problems/majority-element/>

    **Constraints:**

    - `n == nums.length`
    - `1 <= n <= 5 * 10^4`
    - `-10^9 <= nums[i] <= 10^9`

    **Problem:**

    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. 
    You may assume that the majority element always exists in the array.
    """

    def majorityElement(self, nums: List[int]) -> int:
        """
        **Implementation Notes:**
        
        The trick is to use a competing counter `m`, which can be increamented and decreamented 
        by one based whether the current majority result value `r` is equal to current iterated
        item in the array. The loop begins with `r = nums[0]` and `m = 1`. If the next value of 
        `nums` happens to equal to `r`, then we increase `m` by one; If not, descrease `m` by one. 
        When `m` reaches `0`, it indicates that all processed items have resulted in a tie so far.
        The process continue till completion; The final value of `r` will be the majority winner.

        This implementation would be in linear O(N) time and O(1) space.

        **DocTest:**
        
        >>> s = Solution()

        >>> nums = [3,2,3]
        >>> s.majorityElement(nums)
        3

        >>> nums = [2,2,1,1,1,2,2]
        >>> s.majorityElement(nums)
        2

        >>> nums = [2]
        >>> s.majorityElement(nums)
        2
        
        >>> nums = [0, 0]
        >>> s.majorityElement(nums)
        0
        """

        m, r = 0, 0
        for x in nums:
            if m == 0:
                r = x
            
            if r == x:
                m += 1
            else:
                m -= 1
        return r
            
    def majorityElementWithMap(self, nums: List[int]) -> int:
        """
        **Implementation Notes:**

        This implementation would be in linear O(N) time and O(N) space.
        """
        m = {}
        n = len(nums)
        for x in nums:
            if x in m:
                m[x] += 1
            else:
                m[x] = 1
            if m[x] > n/2:
                return x
        
        raise AssertionError("It's supposed to always have a majority element.")


        
def _doctest():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()