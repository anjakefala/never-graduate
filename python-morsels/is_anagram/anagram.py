import string

def is_anagram(a, b):

    excluded = list(string.punctuation) + [' ']
    a = [letter.lower() for letter in a if letter not in excluded]
    b = [letter.lower() for letter in b if letter not in excluded]

    if len(a) != len(b):
        return False

    a.sort()
    b.sort()

    for i, j in zip(a, b):
        if i != j:
            return False

    return True
