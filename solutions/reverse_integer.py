class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        is_negative = True if x < 0 else False

        x_str = str(abs(x))
        reversed = ''
        for c in x_str:
            reversed = c + reversed

        x_int = int(reversed)
        solution = -x_int if is_negative else x_int
        print(solution)
        return solution

    def reverse2(self):
        s = cmp(x, 0)
        r = int(`s * x`[::-1])
        return s * r * (r < 2 ** 31)


# Valid: positive
solution = Solution().reverse(321)
assert solution == 123

# Valid: negative
solution = Solution().reverse(-321)
assert solution == -123
