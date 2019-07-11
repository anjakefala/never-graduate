import string

def letters_in(word):
    excluded = list(string.punctuation) + [' ']
    return sorted(
            char
            for char in word.lower()
            if char not in excluded
        )

def is_anagram(a, b):

    a, b = a.lower(), b.lower()
    return letters_in(a) == letters_in(b)

