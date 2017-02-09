class Solution(object):
    def reverse_int(self, x):

        negative = False
        if x < 0:
            negative = True
            x = abs(x)

        if x < 10:
            return -x if negative else x

        reversed = x % 10
        first_digits = int(x / 10)

        while first_digits >= 10:
            next_last_digit = first_digits % 10
            first_digits = int(first_digits / 10)
            reversed = (reversed * 10) + next_last_digit

        next_last_digit = first_digits % 10
        reversed = (reversed * 10) + next_last_digit

        return -reversed if negative else reversed

    def isPalindrome(self, x):
        """
        Determine whether an integer is a palindrome. Do this without extra space.

        Definition: a word, phrase, or sequence that reads the same backward as forward,
        e.g., madam or nurses run.

        :type x: int
        :rtype: bool
        """

        reversed = self.reverse_int(x)
        return reversed == x


assert Solution().reverse_int(1234) == 4321
assert Solution().reverse_int(11) == 11
assert Solution().reverse_int(41) == 14
assert Solution().reverse_int(1) == 1
assert Solution().reverse_int(0) == 0
assert Solution().reverse_int(-1) == -1
assert Solution().reverse_int(-134) == -431


# Valid: not palindrome
assert Solution().isPalindrome(1243) is False

# Valid: is palindrome
assert Solution().isPalindrome(1331) is True

# Valid: is palindrome
assert Solution().isPalindrome(131) is True

# Valid: duplicates, palindrome
assert Solution().isPalindrome(11) is True

# Valid: negative
assert Solution().isPalindrome(-2147483648) is False
