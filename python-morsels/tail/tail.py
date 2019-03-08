def tail(sequence, n):

    if n <= 0:
        return []

    tailed_sequence = []

    for el in sequence:
        if len(tailed_sequence) == n and n > 1:
            tailed_sequence = tailed_sequence[1:] + [el]
        elif len(tailed_sequence) == n and n == 1:
            tailed_sequence = [el]
        else:
            tailed_sequence.append(el)

    return tailed_sequence
