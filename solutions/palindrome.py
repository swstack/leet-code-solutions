class Solution(object):
    def isPalindrome(self, x):
        """
        Determine whether an integer is a palindrome. Do this without extra space.

        Definition: a word, phrase, or sequence that reads the same backward as forward,
        e.g., madam or nurses run.

        :type x: int
        :rtype: bool
        """

        # O(n), remove spaces
        y = ""
        for i in x.split(" "):
            y += i

        # O(n), reverse the string
        reversed = ''
        for c in y:
            reversed = c + reversed

        solution = y == reversed
        print(solution)
        return solution


# Valid: one word
solution = Solution().isPalindrome("madam")
assert solution == True

# Valid: two words
solution = Solution().isPalindrome("nurses run")
assert solution == True

# Invalid: single word
solution = Solution().isPalindrome("foo")
assert solution == True