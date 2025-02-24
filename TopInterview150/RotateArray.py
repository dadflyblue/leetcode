from typing import List

class Solution:
    """
    The problem link: <https://leetcode.com/problems/rotate-array/>

    **Constraints:**

    - `1 <= nums.length <= 10^5`
    - `-2^31 <= nums[i] <= 2^31 - 1`
    - `0 <= k <= 10^5`

    **Problem:**

    Given an integer array nums, rotate the array to the right by k steps, 
    where k is non-negative.

    **Follow up:**

    - Try to come up with as many solutions as you can. There are at least 
    three different ways to solve this problem.
    - Could you do it in-place with O(1) extra space?

    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        **Implementation Notes:**
        
        This problem is easy to come up with a solution that uses a auxiliary array,
        which requires O(N) space. One trick to get rid of the auxiliary array is to 
        reverse three substrings: all, 0-k, k-n; In this case, it uses only O(1) space.
        
        Both solutions have a linear time complexity of O(N), as they have to walk 
        through the entire input array for copying or reversing operations. 

        **DocTest:**

        >>> s = Solution()

        >>> nums, k = [1,2,3,4,5,6,7], 3
        >>> s.rotate(nums, k)
        >>> nums
        [5, 6, 7, 1, 2, 3, 4]

        >>> nums, k = [1,2,3,4,5,6,7], 10
        >>> s.rotate(nums, k)
        >>> nums
        [5, 6, 7, 1, 2, 3, 4]

        >>> nums, k = [1,2,3,4,5,6,7], 5
        >>> s.rotate(nums, k)
        >>> nums
        [3, 4, 5, 6, 7, 1, 2]

        >>> nums, k = [-1,-100,3,99], 2
        >>> s.rotate(nums, k)
        >>> nums
        [3, 99, -1, -100]

        """
        n = len(nums)
        k = k % n
        
        self._reverse(nums, 0, n-1)
        self._reverse(nums, 0, k-1)
        self._reverse(nums, k, n-1)

    def _reverse(self, nums: List[int], start: int, stop: int):
        while start < stop:
            nums[start], nums[stop] = nums[stop], nums[start]
            start += 1
            stop -= 1

    def rotateWithAuxiliaryArray(self, nums: List[int], k: int) -> None:
        """
        **Implementation Notes:**

        This implementation would be in linear O(N) time and O(N) space.
        """

        n = len(nums)
        # Only the remainder matters;
        # The others will not actually have an effect.
        k = k % n
        # Convert k to the leftward location
        k = n - k
        # Use an auxiliary array for rotating
        aux = nums[k:n] + nums[0:k]
        # Copy the auxiliary arry back to nums
        for i in range(n):
            nums[i] = aux[i]


def _doctest():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()