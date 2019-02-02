def compact(sequence):
    if not sequence:
        return sequence

    if type(sequence) is list:
        sequence = iter(sequence)

    new_iter = [next(sequence)]

    for val in sequence:
        if val != new_iter[-1]:
            new_iter.append(val)
        else:
            continue

    return new_iter
