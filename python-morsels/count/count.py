from collections import defaultdict
import unicodedata as ud

def count_words(sentence):
    count = defaultdict(int)

    for word in sentence.split():

        # strip punctuation from the beginning and end of word
        # we are using ud.category() since string.punctuation only contains ascii punctuation
        word = word[1:] if ud.category(word[0]).startswith('Po') else word
        word = word[:-1] if ud.category(word[-1]).startswith('Po') else word

        count[word.lower()] += 1
    return count
