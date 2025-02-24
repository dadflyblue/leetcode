from typing import List

class Solution:
    """
    The problem link: <https://leetcode.com/problems/remove-duplicates-from-sorted-array>

    **Constraints:**

    - `1 <= nums.length <= 3 * 10^4`
    - `-100 <= nums[i] <= 100`  
    - `nums is sorted in non-decreasing order.`  

    **Problem:**

    Given an integer array nums sorted in non-decreasing order, 
    remove the duplicates in-place such that each unique element appears only once. 
    The relative order of the elements should be kept the same. 
    Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, 
    you need to do the following things:

    - Change the array nums such that the first k elements of nums contain the unique elements 
    in the order they were present in nums initially. 
    The remaining elements of nums are not important as well as the size of nums.
    - Return k.

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

        We simply pick each item into variable `x` from the input array through a `for` loop, 
        and identify distinct items and replace them into the original array. Specifically, 
        in each iteration we compare `x` with the item at postion `k-1`, which holds the most 
        recent unique item found. If the value of `x` equals to the value at positon `k-1`,
        it indicates a duplicate, and we skip this item. If the value of `x` doesn't equal to 
        the value at position `k-1`, it indicates a new unique item found; in this case, we 
        place this unique item at position `k` and increse `k` by one for marking the new postion. 
        As initilization, we place the first `x` as first found unique item at location `k` when 
        it is equal to `0`.

        This implementation would be in linear O(N) time and O(1) space.

        **DocTest:**

        >>> s = Solution()

        >>> nums = [1,1,2]
        >>> s.removeDuplicates(nums)
        2
        >>> nums[:2]
        [1, 2]

        >>> nums = [0,0,1,1,1,2,2,3,3,4]
        >>> s.removeDuplicates(nums)
        5
        >>> nums[:5]
        [0, 1, 2, 3, 4]
        """

        k = 0
        for x in nums:
            if k == 0 or nums[k-1] != x:
                nums[k] = x
                k += 1
        return k


def _doctest():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()