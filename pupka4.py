def del_from_tuple(tpl, q):
    lst = list(tpl)
    if q in tpl:
        lst.remove(q)
    return tuple(lst)