def multimax(sequence, key=max):
    curr_max = []
    for i in sequence:
        if not curr_max:
            curr_max.append(i)
        else:
            if i > curr_max[0]:
                curr_max = [i]
            elif i == curr_max[0]:
                curr_max.append(i)
    return curr_max

