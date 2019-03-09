from collections import deque

def tail(sequence, n):

    if n <= 0:
        return []

    tailed_sequence = deque(maxlen=n)

    for el in sequence:
        tailed_sequence.append(el)

    return list(tailed_sequence)
