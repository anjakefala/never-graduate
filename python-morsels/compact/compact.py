def compact(sequence):
    if not sequence:
        return sequence

    new_iter = [sequence[0]]

    for val in sequence[1:]:
        if val != new_iter[-1]:
            new_iter.append(val)
        else:
            continue

    return new_iter
