def multimax(sequence, key=max):

    return [i for i in sequence if i == key(sequence)]
