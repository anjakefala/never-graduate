from collections import defaultdict

def group_by(sequence, key_func=lambda x: x):
    grouped = defaultdict(list)

    for val in sequence:
        grouped[key_func(val)].append(val)

    return grouped
