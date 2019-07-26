def multimax(sequence, key=None):

    return [i for i in sequence if i == key(sequence)]
