from typing import List

class Solution:
    """
    The problem linke: <https://leetcode.com/problems/jump-game/>
    
    **Constraints:**

    - `1 <= nums.length <= 10^4`
    - `0 <= nums[i] <= 10^5`

    **Problem:**

    You are given an integer array nums. You are initially positioned at 
    the array's first index, and each element in the array represents your 
    maximum jump length at that position. Return true if you can reach the 
    last index, or false otherwise.

    """

    def canJump(self, nums: List[int]) -> bool:
        """
        **Implementation Notes:**

        **DocTest:**

        >>> s = Solution()

        >>> nums = [2,3,1,1,4]
        >>> s.canJump(nums)
        True

        >>> nums = [3,2,1,0,4]
        >>> s.canJump(nums)
        False

        >>> nums = [0]
        >>> s.canJump(nums)
        True

        >>> nums = [0,2,3]
        >>> s.canJump(nums)
        False
        """

        n = len(nums)
        d, r = 1, True
        i = n-2
        while i >= 0:
            if nums[i] >= d:
                r = True
                d = 1
            else:
                r = False
                d += 1
            i -= 1
        return r



def _doctest():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()