class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(nums) < 2:
            print("No solution")
            return None, None

        # O(n^2)
        found = False
        for i, inum in enumerate(nums):
            for j, jnum in enumerate(nums):
                if i == j:
                    continue

                if inum + jnum == target:
                    found = True
                    break
            if found:
                break

        if found:
            s = i, j
            print(s)
            return s
        else:
            print("No solution")
            return None, None


# Valid: all unique
solution = Solution().twoSum([2, 7, 11, 15], 9)
assert solution == (0, 1)

# Valid: duplicates
solution = Solution().twoSum([0, 7, 11, 0], 0)
assert solution == (0, 3)

# Valid: negative numbers
solution = Solution().twoSum([-3, 4, 3, 90], 0)
assert solution == (0, 2)

# Invalid: not enough nums
solution = Solution().twoSum([2], 9)
assert solution == (None, None)

# Invalid: no solution
solution = Solution().twoSum([2, 20, 11, 15], 9)
assert solution == (None, None)
