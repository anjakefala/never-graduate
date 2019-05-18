def count_bits(x):
    '''counts the number of bits in a twos-complement binary value'''
    num_bits = 0
    # shifted positive integers shift to 0
    # shifted negative integers shift to -1
    while x and x != -1:
        # evaluating whether the rightmost binary digit contains a 1
        num_bits += x & 1
        # shift the binary value over to the right
        x >>= 1
    return num_bits


def parity(x):
    return 1 if count_bits(x) % 2 else 0
