class Solution(object):
    def isPalindrome(self, x):
        """
        Determine whether an integer is a palindrome. Do this without extra space.

        Definition: a word, phrase, or sequence that reads the same backward as forward,
        e.g., madam or nurses run.

        :type x: int
        :rtype: bool
        """




# Valid: 3 digit
solution = Solution().isPalindrome(123)
assert solution == 321

# Valid: 2 digit
solution = Solution().isPalindrome(23)
assert solution == True

# Valid: 1 digit
solution = Solution().isPalindrome(1)
assert solution == True

# Valid: duplicates
solution = Solution().isPalindrome(11)
assert solution == True
