from typing import List

class Solution:
    """
    The problem link: <https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii>

    **Constraints:**

    - `1 <= nums.length <= 3 * 10^4` 
    - `-10^4 <= nums[i] <= 10^4`  
    - `nums is sorted in non-decreasing order.` 

    **Problme:**

    Given an integer array nums sorted in non-decreasing order, 
    remove some duplicates in-place such that each unique element appears at most twice. 
    The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, 
    you must instead have the result be placed in the first part of the array nums. More formally, 
    if there are k elements after removing the duplicates, 
    then the first k elements of nums should hold the final result. 
    It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. 
    You must do this by modifying the input array in-place with O(1) extra memory.

    **Custom Judge:**

    The judge will test your solution with the following code:
    ```
    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
    ```
    If all assertions pass, then your solution will be accepted.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        **Implementation Notes:**

        The overall strategy is to identify repeating patterns in the input array,
        through a nested loop with variables `i` and `j`, and compress these duplicate items 
        into two identical items, and place them in positions marked by variable `k` and `k+1`; 
        In this case, we increases `k` by two for marking new position. If no duplicates are found, 
        we simply place the single item in poistion `k` and increase `k` by one.

        This implementation would be in linear O(N) time and O(1) space.

        **DocTest:**

        >>> s = Solution()

        >>> nums = [1,1,1,2,2,3]
        >>> s.removeDuplicates(nums)
        5
        >>> nums[:5]
        [1, 1, 2, 2, 3]

        >>> nums = [0,0,1,1,1,1,2,3,3]
        >>> s.removeDuplicates(nums)
        7
        >>> nums[:7]
        [0, 0, 1, 1, 2, 3, 3]

        >>> nums = [1,1,1]
        >>> s.removeDuplicates(nums)
        2
        >>> nums[:2]
        [1, 1]

        >>> nums = [1,2,3,4,5]
        >>> s.removeDuplicates(nums)
        5
        >>> nums[:5]
        [1, 2, 3, 4, 5]
        """

        k, i, j = 0, 0, 0
        n = len(nums)
        while j < n:
            i = j
            while j < n and nums[i] == nums[j]:
                j += 1
            
            if j-i > 1: # found duplicates
                nums[k], nums[k+1] = nums[i], nums[i]
                k += 2
            else:
                nums[k] = nums[i]
                k += 1
        return k


def _doctest():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()