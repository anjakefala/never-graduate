import string

def is_anagram(a, b):

    # normalise the two lists: all lowercase, no spaces and no punctuation
    excluded = list(string.punctuation) + [' ']
    a = [letter.lower() for letter in a if letter not in excluded]
    b = [letter.lower() for letter in b if letter not in excluded]

    # zip is going to iterate until the shortest string runs out of length
    # since to be a proper anagram, they need to be the same length
    # check for length first
    if len(a) != len(b):
        return False

    # sort after checking for length
    # if they are wrong length, you will not pay the time cost of sorting first
    a.sort()
    b.sort()

    for i, j in zip(a, b):
        if i != j:
            return False

    return True
