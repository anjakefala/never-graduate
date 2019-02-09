def compact(sequence):
    if not sequence:
        return sequence

    if type(sequence) is list:
        sequence = iter(sequence)

    last_value = next(sequence)
    yield last_value

    for val in sequence:
        if val != last_value:
            last_value = val
            yield val
        else:
            continue
