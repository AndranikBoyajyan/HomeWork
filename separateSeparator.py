def separate_separator(a, b):

    while b > 0:
        a, b = b, a % b
    return a
