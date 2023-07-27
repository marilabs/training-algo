def min_sprod(v1, v2):
    v1b = sorted(v1)
    v2b = sorted(v2)
    return sum([v1b[i] * v2b[-i - 1] for i in range(len(v1))])