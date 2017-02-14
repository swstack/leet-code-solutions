def make_combos(options, length):
    """Create len(options)^length combinations

    Example:

        make_combos((a, b), 3)

        options = (a, b)
        length = 3

        len(options) ^ length == 2 ^ 3 == 8

        [a, a, a]
        [a, a, b]
        [a, b, b]
        [a, b, a]
        [b, b, b]
        [b, b, a]
        [b, a, a]
        [b, a, b]

    :return: list of combos
    """
