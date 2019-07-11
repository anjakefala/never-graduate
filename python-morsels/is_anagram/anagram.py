import string

def letters_in(word):
    return sorted(
            char
            for char in word.lower()
            if char.isalpha()
        )

def is_anagram(a, b):

    a, b = a.lower(), b.lower()
    return letters_in(a) == letters_in(b)

