def sieve(lst):
    q = []
    [q.append(item) for item in reversed(lst) if item not in q]
    return tuple(q)