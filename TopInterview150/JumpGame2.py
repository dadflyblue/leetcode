from typing import List

class Solution:
    """

    >>> s = Solution()

    >>> nums = [2,3,1,1,4]
    >>> s.jump(nums)
    2

    >>> nums = [2,3,0,1,4]
    >>> s.jump(nums)
    2

    >>> nums = [2,3,1]
    >>> s.jump(nums)
    1

    >>> nums = [0]
    >>> s.jump(nums)
    0

    >>> nums = [4,1,1,3,1,1,1]
    >>> s.jump(nums)
    2

    >>> nums = [3,1,1,1,1]
    >>> s.jump(nums)
    2

    >>> nums = [1,2,1,1,1]
    >>> s.jump(nums)
    3

    >>> nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
    >>> s.jump(nums)
    2

    >>> nums = [1,1,1,1]
    >>> s.jump(nums)
    3
    """
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        i, j, r = 0, 0, 0 
        while i < n-1:
            j = i + nums[i]
            if j >= n-1:
                r += 1
                break
            k, m = i, j
            while i < j:
                i += 1
                if i + nums[i] > m:
                    m = i + nums[i]
                    k = i
            r += 1
            i = k
        return r


def _doctest():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _doctest()