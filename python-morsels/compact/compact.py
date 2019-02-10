def compact(sequence):
    if not sequence:
        return sequence

    previous = object()

    for val in sequence:
        if val != previous:
            yield val
            previous = val
