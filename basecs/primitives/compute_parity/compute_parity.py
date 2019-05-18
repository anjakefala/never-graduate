def count_bits(x):
    '''currently only works for positive integers'''
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


def parity(x):
    return 1 if count_bits(x) % 2 else 0
