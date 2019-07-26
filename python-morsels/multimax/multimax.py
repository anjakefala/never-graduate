def same(val):
    return val

def multimax(sequence, key=same):
    curr_max = []
    for i in sequence:
        if not curr_max:
            curr_max.append(i)
        else:
            if max(key(i), key(curr_max[0])) == key(i):
                if key(i) != key(curr_max[0]):
                    curr_max = [i]
                else:
                    curr_max.append(i)
    return curr_max

