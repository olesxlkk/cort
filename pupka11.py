def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return ()
    return tuple(sorted(tpl))