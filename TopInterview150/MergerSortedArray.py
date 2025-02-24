from typing import List

class Solution:
    """
    The problem link: <https://leetcode.com/problems/merge-sorted-array/>

    Do not return anything, modify nums1 in-place instead.
    
    **Constraints:**

    - `nums1.length == m + n`
    - `nums2.length == n` 
    - `0 <= m, n <= 200` 
    - `1 <= m + n <= 200` 
    - `-10^9 <= nums1[i], nums2[j] <= 10^9`  

    **Problem:**

    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
    and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.

    The final sorted array should not be returned by the function, 
    but instead be stored inside the array nums1. To accommodate this, 
    nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
    and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        **Implementation Notes:**

        The trick is to merge two arrays from the end, which appears much easier than merging 
        them from the beginning which I haven't figured out yet.

        This implementation would be in linear O(N) time and O(1) space.

        **DocTest:**

        >>> s = Solution()

        >>> nums1, m = [1,2,3,0,0,0], 3
        >>> nums2, n = [2,5,6], 3
        >>> s.merge(nums1, 3, nums2, 3)
        >>> nums1
        [1, 2, 2, 3, 5, 6]

        >>> nums1, m = [1], 1, 
        >>> nums2, n = [], 0
        >>> s.merge(nums1, 1, nums2, 0)
        >>> nums1
        [1]

        >>> nums1, m = [0], 0
        >>> nums2, n = [1], 1
        >>> s.merge(nums1, 0, nums2, 1)
        >>> nums1
        [1]

        """

        j, k = m-1, n-1
        for i in range(m+n-1, -1, -1):
            if j >= 0 and k >= 0:
                if nums1[j] > nums2[k]:
                    nums1[i] = nums1[j]
                    j -= 1
                else:
                    nums1[i] = nums2[k]
                    k -= 1
            elif j < 0:
                nums1[i] = nums2[k]
                k -= 1
            else:
                nums1[i] = nums1[j]
                j -= 1


def _doctest():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()