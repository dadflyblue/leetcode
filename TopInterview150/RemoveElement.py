from typing import List

class Solution:
    """
    The problem link: <https://leetcode.com/problems/remove-element/>

    **Constraints:**

    - `0 <= nums.length <= 100`
    - `0 <= nums[i] <= 50`  
    - `0 <= val <= 100`  

    **Problem:**

    Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
    The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

    Consider the number of elements in nums which are not equal to val be k, 
    to get accepted, you need to do the following things:

    - Change the array nums such that the first k elements of nums contain the elements 
    which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    - Return k.

    **Custom Judge:**

    The judge will test your solution with the following code:
    ```
    int[] nums = [...]; // Input array  
    int val = ...; // Value to remove  
    int[] expectedNums = [...]; // The expected answer with correct length.  
                                // It is sorted with no values equaling val.  

    int k = removeElement(nums, val); // Calls your implementation  

    assert k == expectedNums.length;  
    sort(nums, 0, k); // Sort the first k elements of nums  
    for (int i = 0; i < actualLength; i++) {  
        assert nums[i] == expectedNums[i];  
    }  
    ```
    If all assertions pass, then your solution will be accepted.  
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        **Implementation Notes:**

        The trick is to replace the item euqal to `val` in input array with the item 
        at the end of the array, and then shorten the array by decreasing the variable `k` 
        by one. The variable `k` is used to indicate the actual ending postion of the array.

        This implementation would be in linear O(N) time  and O(1) space.

        **DocTest:**

        >>> s = Solution()
        
        >>> nums, val = [3,2,2,3], 3
        >>> s.removeElement(nums, val)
        2
        >>> sorted(nums[:2])
        [2, 2]

        >>> nums, val = [0,1,2,2,3,0,4,2], 2
        >>> s.removeElement(nums, val)
        5
        >>> sorted(nums[:5])
        [0, 0, 1, 3, 4]
        """

        i = 0
        k = len(nums)
        while i < k:
            if nums[i] == val:
                # replace with the last element and keep i unchanged
                # to make sure it will be checked next round.
                nums[i] = nums[k-1]
                k -= 1
            else:
                i += 1
        return k


def _doctest():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()