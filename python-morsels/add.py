def add(*arrs):
    return [
            [sum(values) for values in zip(*rows)]
            for rows in zip(*arrs)
            ]
