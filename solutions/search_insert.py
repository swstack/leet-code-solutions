class Solution(object):
    def searchInsert(self, nums, target):
        """
        Given a sorted array and a target value, return the index if the target is found. If not,
        return the index where it would be if it were inserted in order.

        You may assume no duplicates in the array.

        Here are few examples.
        [1,3,5,6], 5 → 2
        [1,3,5,6], 2 → 1
        [1,3,5,6], 7 → 4
        [1,3,5,6], 0 → 0

        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i, n in enumerate(nums):
            current_num = n
            last_num = nums[i - 1] if i > 0 else None

            if last_num is None and target < current_num:
                return 0

            if current_num == target:
                return i

            if last_num and last_num < target < current_num:
                return i

        return i + 1


# Valid: middle
solution = Solution().searchInsert([1, 3, 5, 6], 5)
assert solution == 2

# Valid: last
solution = Solution().searchInsert([1, 3, 5, 6], 10)
assert solution == 4

# Valid: first
solution = Solution().searchInsert([1, 3, 5, 6], 0)
assert solution == 0

# Valid: negative target
solution = Solution().searchInsert([1, 3, 5, 6], -1)
assert solution == 0

# Valid: negative list
solution = Solution().searchInsert([-1, 3, 5, 6], -1)
assert solution == 0

# Valid: short list
solution = Solution().searchInsert([1, 3], 2)
assert solution == 1
