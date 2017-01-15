class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """


# Valid: positive
solution = Solution().convert(321)
assert solution == 123

# Valid: negative
solution = Solution().convert(-321)
assert solution == -123